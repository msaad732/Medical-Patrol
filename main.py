import os
import requests
from openai import OpenAI
from flask import Flask, render_template, request, jsonify
import smtplib
from email.mime.text import MIMEText
from fetch_agent import run_agent_case_report


# Email Alert
def send_email_alert(subject, message):
    sender = "meizsaad732@gmail.com"
    receiver = "ekhaliq409@gmail.com"
    password = os.getenv("EMAIL_PASSWORD")  # Store securely

    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = receiver

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.send_message(msg)
        print("✅ Email sent.")
    except Exception as e:
        print("❌ Failed to send email:", e)


# OCR Function
def extract_text_from_image(image_path):
    url = 'https://api.ocr.space/parse/image'
    payload = {
        'apikey': 'K84294023988957',  # Replace with your actual OCR API key
        'language': 'eng',
    }
    with open(image_path, 'rb') as f:
        files = {'filename': (image_path, f)}
        r = requests.post(url, data=payload, files=files)
        result = r.json()
        try:
            return result['ParsedResults'][0]['ParsedText']
        except (KeyError, IndexError):
            return "Could not extract text from image."


# Groq LLaMA-3 Setup
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),  # Store in environment
    base_url="https://api.groq.com/openai/v1")

# In-memory conversation store (MCP style)
conversations = {}


def ask_groq_llama(prompt, user_id="user-1"):
    if user_id not in conversations:
        conversations[user_id] = [{
            "role":
            "system",
            "content":
            "You're a concise medicine verification assistant. Reply briefly."
        }]

    conversations[user_id].append({"role": "user", "content": prompt})

    response = client.chat.completions.create(model="llama3-8b-8192",
                                              messages=conversations[user_id],
                                              max_tokens=150,
                                              temperature=0.5,
                                              user=user_id)

    reply = response.choices[0].message.content.strip()
    conversations[user_id].append({"role": "assistant", "content": reply})
    return reply


# Flask Setup
app = Flask(__name__)
app.secret_key = "any_random_key"
app.config["UPLOAD_FOLDER"] = "uploads"

if not os.path.exists("uploads"):
    os.makedirs("uploads")


# Routes
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/transcribe", methods=["POST"])
def transcribe():
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file"}), 400

    try:
        audio_file = request.files["audio"]

        response = client.audio.transcriptions.create(model="whisper-large-v3",
                                                      file=audio_file,
                                                      response_format="text")
        return jsonify({"text": response})

    except Exception as e:
        print(f"Transcription error: {e}")
        return jsonify({
            "error": "Transcription failed",
            "details": str(e)
        }), 500


@app.route("/check", methods=["POST"])
def check():
    image = request.files.get("image")
    if not image:
        return jsonify({"error": "No image provided."}), 400

    image_path = os.path.join(app.config["UPLOAD_FOLDER"], "upload.jpg")
    image.save(image_path)

    text = extract_text_from_image(image_path)
    prompt = f"Can you verify if this medicine is fake or authentic?\n\n{text}"
    result = ask_groq_llama(prompt)

    response_data = {
        "text_from_image": text,
        "groq_response": result,
        "email_sent": False
    }

    if "fake" in result.lower() or "counterfeit" in result.lower():
        send_email_alert("⚠️ Fake Medicine Detected",
                         f"Text:\n{text}\n\nReply:\n{result}")
        run_agent_case_report(text, result)
        response_data["email_sent"] = True

    return jsonify(response_data)


@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    prompt = data.get("prompt", "")
    user_id = data.get("user", "user-1")

    if not prompt:
        return jsonify({"error": "No prompt provided."}), 400

    response = ask_groq_llama(prompt, user_id=user_id)
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)
