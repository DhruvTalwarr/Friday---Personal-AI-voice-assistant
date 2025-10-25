import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

def speak(audio):
    # print("=====Friday not activated yet=====\n")
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[2].id) # Make SURE this index is correct
    engine.setProperty("rate", 170)
    print(f"Friday: {audio}") 
    engine.say(audio)
    engine.runAndWait()
    
    # VERY IMPORTANT: Stop/Quit the engine to free up the SAPI resource
    engine.stop() 
    del engine 

dictapp = { "commandprompt": "cmd",
        "paint": "mspaint",
        "word": "winword",
        "excel": "excel",
        "powerpoint": "powerpnt",
        "notepad": "notepad",
        "calculator": "calc",
        "calendar": "outlookcal",
        "chrome": "chrome",
        "vscode": "code",
        "spotify": "spotify",
        "wordpad": "write",
}

def openappweb(query):
    speak("Launching, sir")
    if ".com" in query or "co.in" in query or ".org" in query:
        query = query.replace("open", "")
        query = query.replace("launch", "")
        query = query.replace("website", "")
        query = query.replace("web", "")
        query = query.replace("site", "")
        query = query.replace(" ", "")
        web1 = "https://www." + query
        webbrowser.open(web1)
        speak("Done, sir")
    
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")

def closeapp(query):
    speak("Closing, sir")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")
        speak("Closed one tab, sir")

    elif "2 tabs" in query or "two tabs" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("Closed two tabs, sir")

    elif "3 tabs" in query or "three tabs" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        speak("Closed three tabs, sir")

    elif "4 tabs" in query or "four tabs" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("Closed four tabs, sir")

    elif "5 tabs" in query or "five tabs" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("Closed five tabs, sir")

    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")
        speak("Done, sir")