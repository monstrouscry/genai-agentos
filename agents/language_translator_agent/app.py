from flask import Flask, request, jsonify
from flask_ngrok import run_with_ngrok
from translator_agent import TranslatorAgent
import os

app = Flask(__name__)
run_with_ngrok(app)  # Automatically exposes via ngrok

# Load OpenAI API key from environment variable
agent = TranslatorAgent(openai_api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def index():
    return """
    <h3>✅ Translator Agent is Running</h3>
    <p>Use <code>/translate</code> endpoint via POST or GET</p>
    <ul>
        <li>GET format: <code>/translate?text=Hello&source_lang=English&target_lang=Marathi</code></li>
        <li>POST format: JSON body with <code>text</code>, <code>source_lang</code>, <code>target_lang</code></li>
    </ul>
    """

@app.route("/translate", methods=["GET", "POST"])
def translate():
    if request.method == "POST":
        data = request.get_json()
        text = data.get("text")
        source_lang = data.get("source_lang")
        target_lang = data.get("target_lang")
    else:
        text = request.args.get("text")
        source_lang = request.args.get("source_lang")
        target_lang = request.args.get("target_lang")

    if not all([text, source_lang, target_lang]):
        return jsonify({"error": "Missing parameters"}), 400

    # Optional Bonus: detect idiom (basic placeholder logic)
    idioms = ["raining cats and dogs", "break the ice", "once in a blue moon"]
    is_idiom = any(phrase in text.lower() for phrase in idioms)

    translated = agent.translate(text, source_lang, target_lang)

    if request.method == "GET":
        return f"""
            <h3>📝 Original Text:</h3><p>{text}</p>
            <h3>🔁 Translated ({source_lang} → {target_lang}):</h3>
            <p>{translated}</p>
            {'<p>💡 Idiom detected!</p>' if is_idiom else ''}
        """
    else:
        return jsonify({
            "original_text": text,
            "source_language": source_lang,
            "target_language": target_lang,
            "translation": translated,
            "idiom_detected": is_idiom
        })

if __name__ == "__main__":
    app.run()  # ⚠️ No debug=True with flask-ngrok

