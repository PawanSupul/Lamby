import openai
from PyQt5.QtCore import pyqtSignal, QObject
# from data_io import Json_IO

class ConversationEngine(QObject):
    response_ready = pyqtSignal(dict)
    
    def __init__(self):
        super().__init__()
        self.words = ["pan", "como", "comes", "agua", "leche", "bebe", "bebo", "bebes"]
        self.conversation_history = []
        self.set_key()

    def set_key(self):
        key_file = 'secrets/openai.txt'
        with open(key_file, 'r') as fid:
            api_key = fid.read()
        openai.api_key = api_key

    def get_conversation_reply(self, user_text):
        if user_text.lower() in ["exit", "quit", "bye"]:
            output = {'status': 0, 'text': '¡Adiós! ¡Que tengas un buen día!'}
        else:
            self.conversation_history.append({"role": "user", "content": user_text})

            system_instruction = (
                "Teach Spanish to beginners through simple conversation. "
                "Speak in Spanish, use simple words, correct mistakes in English, and reply in English only when necessary."
                f"Focus the conversation around these words: {', '.join(self.words)}."
            )

            response = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system",
                     "content": system_instruction},
                    *self.conversation_history
                ],
                max_tokens=100
            )
            bot_reply = response.choices[0].message.content
            self.conversation_history.append({"role": "assistant", "content": bot_reply})
            output = {'status': 1, 'text': bot_reply}

        # return output
        self.response_ready.emit(output)


    def reset_conversation(self):
        self.conversation_history = []


if __name__ == '__main__':
    c_engine = ConversationEngine()
    reply = c_engine.get_conversation_reply('Hey my name is pawan')
    print(reply)