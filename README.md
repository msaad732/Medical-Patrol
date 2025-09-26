# 🏥 Medical Patrol – AI-Powered Counterfeit Medicine Detection  

Medical Patrol is an **AI-powered web application** built to fight the dangerous rise of counterfeit medicines, particularly in underserved regions like **Africa**.  

This project was developed during the **Raise Your Hack Hackathon (July 4–8)** with the mission of **protecting lives through technology**.  

🔗 **Project Link:** [Medical Patrol](https://lnkd.in/dG6Ff48J)  

---

## 🚨 Why Medical Patrol?  

Counterfeit medicines are a **global health crisis**, leading to:  
- Failed treatments  
- Worsening conditions  
- Preventable deaths  

**Medical Patrol** empowers communities with a **quick, accessible, and low-cost verification system** for medicine authenticity.  

---

## ✨ Features  

- 📷 **AI-Powered Authenticity Checks**  
  - Upload a photo of a medicine label.  
  - Uses **OCR (Optical Character Recognition)** to extract text.  
  - Text analyzed by **LLaMA-3 (via Groq)** to detect potential counterfeits.  

- 📧 **Automated Alerts & Case Logging**  
  - Generates detailed case reports with an autonomous agent.  
  - Sends **email alerts** to relevant authorities if a counterfeit is suspected.  

- 🧠 **Voice-Enabled AI Chatbot with Memory**  
  - Users can **speak directly** to the chatbot for real-time medicine queries.  
  - Powered by **Groq’s Whisper** (speech-to-text) + **LLaMA-3** (intelligent replies).  
  - Uses **Model Context Protocol (MCP)** to remember previous conversations for consistent, personalized support.  

---

## 🛠️ Tech Stack  

- **AI/ML & NLP** – LLaMA-3 (via Groq), Whisper  
- **OCR** – OCR.space API for text extraction  
- **Web Framework** – Flask (Python)  
- **Conversational AI** – Voice-enabled chatbot with memory (MCP)  
- **Automation** – Email alerts + autonomous case logging  
- **Frontend** – Responsive web interface  
- **Other Tools** – Computer Vision, Speech Recognition, Real-time AI Integration  

---

## 🚀 Getting Started  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/msaad732/Medical-Patrol.git
cd medical-patrol
````

### 2️⃣ Setup Environment

Create a Python virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)
pip install -r requirements.txt
```

### 3️⃣ Setup Environment Variables

Create a `.env` file in the project root and add API keys:

```env
OCR_API_KEY=your_ocr_api_key
GROQ_API_KEY=your_groq_api_key
EMAIL_USER=your_email
EMAIL_PASS=your_password
```

### 4️⃣ Run the App

```bash
python app.py
```

The app will be available at:
👉 [http://localhost:5000](http://localhost:5000)

---

## 📦 Deployment

You can deploy **Medical Patrol** on:

* **Heroku**
* **Render**
* **Vercel (for frontend only)**
* **AWS / GCP / Azure**

---

## 👨‍💻 Built By

* **Muhammad Saad**
* **Eman Khaliq**

---

## 💡 Inspiration

We built Medical Patrol to support the **#HackForAfrica initiative**, focusing on **social impact** by protecting vulnerable communities from counterfeit medicine.

This project represents more than just technology – it’s about **saving lives through innovation**.

---

## 🛡️ License

This project is licensed under the **MIT License** – feel free to use and modify.

```

Do you also want me to add a **"Screenshots / Demo GIFs" section** so people can visually understand how Medical Patrol works before running it?
```
