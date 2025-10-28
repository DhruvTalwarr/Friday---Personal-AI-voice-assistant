# speaker.py
import pyttsx3

def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 200)
    engine.setProperty('volume', 3.0)
    print(f"Friday: {audio}")
    engine.say(audio)
    engine.runAndWait()


