import pyautogui
import speech_recognition as sr
from speaker import speak  

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 6)
    try:
        print("Understanding...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
    except Exception:
        return "none"
    return query.lower()

def voice_typing_mode():
    speak("Voice typing mode activated. Start speaking, sir.")
    typed_text = ""

    while True:
        query = takeCommand()

        if "stop typing" in query or "friday stop typing" in query:
            speak("Voice typing stopped, sir.")
            speak("Do you want me to enter this message?")
            confirm = takeCommand()

            if any(word in confirm for word in ["yes", "enter", "yeah", "go ahead", "sure"]):
                pyautogui.press('enter')
                speak("Message entered successfully, sir.")
            elif any(word in confirm for word in ["no", "don't", "nope", "cancel", "stop"]):
                speak("Okay sir, returning to normal mode without entering.")
            else:
                speak("I couldn’t understand your response, sir. Returning to normal mode.")
            break

        elif query == "none":
            continue

        else:
            pyautogui.typewrite(query + " ", interval=0.05)
            typed_text += query + " "
            print(f"Typed: {query}")
