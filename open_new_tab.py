import pyautogui
import time
import psutil
import subprocess
import speech_recognition as sr
from speaker import speak


def takeCommand():
    """Listen for user command."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening for browser name...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 5)
    try:
        print("Understanding...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
    except Exception:
        return "none"
    return query.lower()


def is_browser_running():
    browsers = ["chrome.exe", "msedge.exe", "brave.exe"]
    for process in psutil.process_iter(['name']):
        if process.info['name'] and process.info['name'].lower() in browsers:
            return True
    return False


def open_browser(browser_name):
    paths = {
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        "brave": r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
    }

    browser_name = browser_name.lower()
    for key in paths:
        if key in browser_name:
            try:
                subprocess.Popen(paths[key])
                time.sleep(2)
                pyautogui.hotkey('ctrl', 't')
                speak(f"{key.capitalize()} launched and a new tab opened, sir.")
                return
            except Exception:
                speak(f"Sorry sir, I was unable to open {key}.")
                return
    speak("Sorry sir, I couldn't find that browser on your system.")


def open_new_tab():
    speak("Checking for open browsers, sir.")
    time.sleep(0.5)

    if is_browser_running():
        speak("Browser detected. Opening a new tab.")
        pyautogui.hotkey('ctrl', 't')
        speak("New tab opened successfully.")
    else:
        speak("No browser found, sir. Should I open Chrome, Edge, or Brave?")
        browser_choice = takeCommand()
        if "none" in browser_choice or browser_choice == "":
            speak("I didn't get that, sir. Please try again later.")
            return
        open_browser(browser_choice)
