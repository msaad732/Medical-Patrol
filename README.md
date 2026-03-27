# 🏥 Medical Patrol: AI-Powered Counterfeit Medicine Detection

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Groq API](https://img.shields.io/badge/Groq-Fast_AI-orange.svg)](https://groq.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**An intelligent web platform that uses optical character recognition (OCR) and Large Language Models (LLMs) to verify medicine authenticity and alert authorities to counterfeit drugs.**

---

## 🌍 The Big Picture (What is this?)
Counterfeit medicines are a silent global health crisis, particularly in underserved regions across Africa. Fake drugs lead to failed treatments, worsening health conditions, and thousands of preventable deaths every year. 

**Medical Patrol** is built to fight back. It is an accessible, AI-driven web application that allows anyone to quickly verify if their medicine is genuine just by taking a picture or talking to an AI assistant. 

## 💡 The Value (Why does this matter?)
* **Instant Verification:** Replaces guesswork with rapid, AI-backed analysis of medication packaging and labels.
* **Automated Authority Alerts:** It doesn't just warn the patient; an autonomous agent logs the counterfeit case and instantly emails relevant health authorities to take action.
* **Highly Accessible Interface:** Features a voice-enabled AI chatbot (powered by Whisper) with memory, allowing users to ask questions about their medicine out loud—crucial for accessibility in diverse communities.

## 🧠 How It Works (In Plain English)
1. **Snap & Read:** A user uploads a photo of their medicine label. The system uses OCR to extract every piece of text, including batch numbers and active ingredients.
2. **AI Interrogation:** The extracted text is fed into **LLaMA-3** (running at lightning speed via Groq). The AI cross-references the data to spot inconsistencies typical of fake drugs.
3. **Voice Assistance:** If a user has questions, they can speak directly to the app. The AI remembers the context of the conversation (using Model Context Protocol) to provide personalized, intelligent medical support.
4. **Action & Reporting:** If a fake is detected, the system generates a formal case report and fires off automated email alerts.

---

## 📸 See It In Action
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/490d4504-97a5-4819-affa-f37d13df4285" />


---

## 💻 Developer Quick Start

### 1. Installation & Environment
Clone the repository and set up your Python virtual environment:

```bash
git clone [https://github.com/msaad732/Medical-Patrol.git](https://github.com/msaad732/Medical-Patrol.git)
cd medical-patrol
python -m venv venv

# Activate the virtual environment:
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

### 2. Environment Variables
Medical Patrol relies on several external APIs. Create a `.env` file in the root directory and add your credentials:

```env
OCR_API_KEY=your_ocr_space_api_key
GROQ_API_KEY=your_groq_api_key
EMAIL_USER=your_alert_sender_email@gmail.com
EMAIL_PASS=your_email_app_password
```

### 3. Run the Application
Start the Flask development server:

```bash
python app.py
```
The application will be live at: `http://localhost:5000`

---

## 🛠️ Technology Stack
* **Core AI/NLP:** LLaMA-3 (via Groq), Whisper (Speech-to-Text)
* **Computer Vision:** OCR.space API 
* **Backend Framework:** Python / Flask
* **Conversational Infrastructure:** Model Context Protocol (MCP) for persistent chatbot memory
* **Automation:** Python `smtplib` for autonomous reporting and email alerts

---

## 🌱 Project Origins
Medical Patrol was developed during the **Raise Your Hack Hackathon (July 4–8, 2024)**. It was built specifically to support the **#HackForAfrica** initiative, focusing on creating scalable, low-cost social impact technology to protect vulnerable communities. 

**Built By:** 
* Muhammad Saad
* Eman Khaliq
