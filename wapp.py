import pyautogui
import pyperclip
import time
import pyttsx3
import speech_recognition as sr
import pygetwindow as gw

# ------------------ Helper Functions ------------------

def speak(audio):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[2].id)
    engine.setProperty("rate", 170)
    print(f"Friday: {audio}")
    engine.say(audio)
    engine.runAndWait()
    engine.stop()
    del engine

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)
    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except:
        print("Say that again")
        return "None"
    return query

# ------------------ WhatsApp Automation ------------------

def send_whatsapp_message():
    # 1. Bring WhatsApp to front
    windows = gw.getWindowsWithTitle("WhatsApp")
    if not windows:
        speak("Please open WhatsApp Desktop first.")
        return
    whatsapp_window = windows[0]
    whatsapp_window.activate()
    time.sleep(1)

    # 2. Ask for contact
    speak("Who do you want to message?")
    contact_name = takeCommand()
    if contact_name == "None":
        speak("Sorry sir, I didn't catch the contact name.")
        return

    # 3. Ask for message
    speak(f"What message should I send to {contact_name}?")
    message = takeCommand()
    if message == "None":
        speak("Sorry sir, I didn't catch the message.")
        return

    # 4. Click search bar
    search_bar_coords = (200, 100)  # <-- update for your screen
    pyautogui.click(search_bar_coords)
    time.sleep(0.5)

    # 5. Search contact
    pyperclip.copy(contact_name)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.3)
    pyautogui.press('enter')
    time.sleep(1)

    # 6. Paste and send message
    pyperclip.copy(message)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.3)
    pyautogui.press('enter')

    speak(f"Message sent to {contact_name} successfully!")

# ------------------ Main Function ------------------

if __name__ == "__main__":
    speak("Testing WhatsApp message automation.")
    send_whatsapp_message()
