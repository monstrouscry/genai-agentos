from agent.translator_agent import TranslatorAgent
import os

if __name__ == "__main__":
    api_key = os.getenv("OPENAI_API_KEY")
    agent = TranslatorAgent(api_key)

    src = input("Source Language: ")
    tgt = input("Target Language: ")
    text = input("Enter text to translate: ")

    translation = agent.translate(text, src, tgt)
    print("\n🌍 Translated Text:\n", translation)
