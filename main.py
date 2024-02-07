import os
from dotenv import load_dotenv
import google.generativeai as genai
import pyttsx3 as tx
from whisper_mic import WhisperMic
import warnings

load_dotenv()
warnings.filterwarnings(
    "ignore", message="FP16 is not supported on CPU; using FP32 instead")


class autobot:
    def __init__(self):
        self.mic = WhisperMic()

    def bot(self):
        bot_engine = tx.init()
        bot_engine.setProperty('rate', 150)
        bot_engine.say("Hello, I'm Rashmin. What can I do for you?")
        bot_engine.runAndWait()

    def speech(self):
        result = self.mic.listen()
        return result

    def chat(self, searching):
        genai.configure(api_key=os.getenv("API_KEY"))
        config = {"temperature": 0.9, "top_p": 1,
                  "top_k": 1, "max_output_tokens": 500}

        model = genai.GenerativeModel("gemini-pro", generation_config=config)

        response = model.generate_content(searching)

        text = ' '.join([part.text for part in response.parts])
        return text

    def chatbot(self):
        while True:
            searching = self.speech()
            response = self.chat(searching)
            print(response)
            if response.lower() == "disconnect":
                break


if __name__ == "__main__":
    bot = autobot()
    bot.bot()
    bot.chatbot()
