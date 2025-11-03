from speech_recognition import Recognizer, Microphone
from speak import speak
import screen_brightness_control as sbc
from speaker import speak

def adjust_brightness(level=None):
    """
    Adjust screen brightness.
    If no level given, it asks for it via voice.
    """
    try:
        if level is None:
            speak("What brightness level should I set, sir?")
            level = int(input("Enter brightness level (0–100): "))

        sbc.set_brightness(level)
        speak(f"Brightness set to {level} percent.")
    except Exception as e:
        speak("Sorry sir, I was unable to adjust brightness.")
        print(e)

def takeCommand():
    r = Recognizer()
    with Microphone() as source:
        print("Listening...")
        audio = r.listen(source, 0, 4)
    try:
        query = r.recognize_google(audio, language='en-in').lower()
        print(f"You said: {query}")
        return query
    except:
        return "none"

def brightness_control():
    speak("What brightness level should I set, sir?")
    query = takeCommand()

    try:
        # Remove any non-digit characters
        level = int(''.join(filter(str.isdigit, query)))
        if 0 <= level <= 100:
            adjust_brightness(level)
        else:
            speak("Please say a level between zero and hundred.")
    except:
        speak("I could not understand the brightness level. Please try again.")

