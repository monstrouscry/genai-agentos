# 🌐 AI Language Translator Agent

## 🔧 Description
This app translates text from one language to another using OpenAI's GPT and supports both idioms and standard sentences. It supports both GET and POST requests and runs on ngrok for public access.

## 🚀 Features
- 🗣️ Language translation (multi-language)
- 🌍 GET and POST API interface
- 🧠 Basic idiom recognition
- 🔗 ngrok live endpoint
- 🖥️ Browser-friendly output via GET
- 📱 Testable via browser, Postman, or curl

## 📦 Requirements

- Python 3.8+
- Flask
- flask-ngrok
- openai

## 📡 Usage

### Step-by-step:

1. Export your OpenAI API Key (required for translation to work):

For Windows (CMD):
```bash
set OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxx

For Git Bash / PowerShell / Linux / macOS:
export OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxx


1. Run the app:
```bash
python app.py

2. In another terminal, start ngrok:
./ngrok http 5000

3. Copy the generated URL (e.g., https://1efb-203-194-96-48.ngrok-free.app)

4. Open in browser:
https://<your-ngrok>.ngrok-free.app/translate?text=Hello&source_lang=English&target_lang=Hindi

Example idiom:
https://<your-ngrok>.ngrok-free.app/translate?text=It%27s%20raining%20cats%20and%20dogs&source_lang=English&target_lang=Bengali

5. Use curl or Postman:
curl -X POST https://<your-ngrok>.ngrok-free.app/translate \
  -H "Content-Type: application/json" \
  -d '{"text": "Break the ice", "source_lang": "English", "target_lang": "Hindi"}'
