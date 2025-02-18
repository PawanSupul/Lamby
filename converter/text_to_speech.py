import pyttsx3


class TextToSpeech_Microsoft():
    def __init__(self):
        # Initialize TTS engine
        self.engine = pyttsx3.init()

    # Set voice properties
    def set_voice(self, language="en"):
        voices = self.engine.getProperty('voices')
        for voice in voices:
            if language in voice.languages or language in voice.id:
                self.engine.setProperty('voice', voice.id)
                break

    # Function to convert text to speech
    def text_to_speech_file(self, text, lang="en", output_file="output.mp3"):
        self.set_voice(lang)
        self.engine.save_to_file(text, output_file)
        self.engine.runAndWait()
        print(f"Speech saved as {output_file}")


    def text_to_speech(self, text, lang="en"):
        self.set_voice(lang)
        self.engine.say(text)
        self.engine.runAndWait()


if __name__ == '__main__':
    tts = TextToSpeech_Microsoft()
    # Example Usage
    tts.text_to_speech("Hello, how are you?", lang="en")
    tts.text_to_speech("Hola, ¿cómo estás?", lang="es")

