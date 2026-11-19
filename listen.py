
import speech_recognition as sr

recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("ULTRON: Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source, timeout=8)
            text = recognizer.recognize_google(audio)

            print("You:", text)
            return text

        except sr.UnknownValueError:
            return ""

        except sr.RequestError:
            print("Speech recognition service unavailable.")
            return ""

        except sr.WaitTimeoutError:
            return ""
