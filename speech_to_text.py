import queue
import sounddevice as sd
import vosk
import json

class SpeachToText():
    def __init__(self):
        # Set model path (download from https://alphacephei.com/vosk/models)
        model_path_en = "models/vosk-model-small-en-in-0.4"
        model_path_es = "models/vosk-model-small-es-0.42"
        self.model_en = vosk.Model(model_path_en)
        self.model_es = vosk.Model(model_path_es)
        self.rec_en = vosk.KaldiRecognizer(self.model_en, 16000)
        self.rec_es = vosk.KaldiRecognizer(self.model_es, 16000)
        self.q = queue.Queue()

        self.model_select = "en"
        self.break_stt = False


    def set_model(self, m_type):
        self.model_select = m_type


    def toggle_break(self):
        self.break_stt = not self.break_stt


    def callback(self, indata, frames, time, status):
        """Callback function to receive audio data."""
        if status:
            print(status, flush=True)
        self.q.put(bytes(indata))


    def speech_to_text_dynamic(self) -> None:
        with sd.RawInputStream(samplerate=16000, blocksize=8000, device=None,
                               dtype="int16", channels=1, callback=self.callback):
            print("Listening... Speak into the microphone.")

            while True:
                if self.break_stt:
                    break

                data = self.q.get()
                if(self.model_select == "en"):
                    rec = self.rec_en
                elif(self.model_select == "es"):
                    rec = self.rec_es
                else:
                    rec = None

                full_phrase = rec.AcceptWaveform(data)

                if full_phrase:
                    result = json.loads(rec.Result())["text"]
                    print(f"You said EN: {result}")


if __name__ == '__main__':
    stt = SpeachToText()
    stt.speech_to_text_dynamic()
