import openai

class TranslatorAgent:
    def __init__(self, openai_api_key):
        openai.api_key = openai_api_key

    def translate(self, text, source_lang, target_lang):
        prompt = (
            f"You are a professional translator. Translate from {source_lang} to {target_lang}, "
            "making sure the result sounds fluent, natural, and retains idiomatic expressions "
            f"accurately. Original text:\n\n{text}\n\nTranslated:"
        )

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )

        return response['choices'][0]['message']['content'].strip()
