import openai
from PyQt5.QtCore import QRunnable, QThreadPool
# from data_io import Json_IO

class ConversationEngine():
    def __init__(self):
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
            output = {'status': 0, 'text': 'Goodbye! Have a nice day!'}
        else:
            self.conversation_history.append({"role": "user", "content": user_text})

            response = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system",
                     "content": f"Maintain a simple spanish conversation using these words: {', '.join(self.words)}."},
                    *self.conversation_history
                ],
                max_tokens=100
            )
            bot_reply = response.choices[0].message.content
            self.conversation_history.append({"role": "assistant", "content": bot_reply})
            output = {'status': 1, 'text': bot_reply}

        return output


    def reset_conversation(self):
        self.conversation_history = []

if __name__ == '__main__':
    c_engine = ConversationEngine()
    reply = c_engine.get_conversation_reply('Hey my name is pawan')
    print(reply)