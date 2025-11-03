import pyttsx3
import speech_recognition as sr
import pyautogui
import os
import sys
import time
import random
import threading
import webbrowser
from datetime import datetime, timedelta

# ------------------ External Modules ------------------
from GreetMe import greetMe
from WeatherNow import get_weather_data
from SearchNow import searchGoogle, searchYouTube, searchWikipedia
from AlarmSet import set_alarm_with_ring, stop_alarm
from calulator import Calc
from News import latestNews
from Whatsapp import sendMessage
from test_speed import getSpeed
from live_cricket_score import live_cricket_score_interactive
from game import game_play
from keyboard import take_screenshot, volumeup, volumedown
from FocusGraph import focus_graph
from translate import translategl

# ------------------ Speak Function ------------------
def speak(text):
    def run_speech(txt):
        engine = pyttsx3.init("sapi5")
        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[2].id)
        engine.setProperty("rate", 170)
        print(f"Friday: {txt}")
        engine.say(txt)
        engine.runAndWait()
        engine.stop()
        del engine
    threading.Thread(target=run_speech, args=(text,)).start()

# ------------------ Take Command Function ------------------
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
    except Exception:
        print("Say that again")
        return "None"
    return query.lower()

# ------------------ Alarm Handler ------------------
def handle_alarm():
    try:
        set_alarm_with_ring(speak, takeCommand)
    except Exception as e:
        speak("Sorry sir, there was an error setting the alarm.")
        print(f"Alarm Error: {e}")

# ------------------ Main Function ------------------
def main():
    # Password protection
    for i in range(3):
        a = input("Enter password to open Friday: ")
        with open("password.txt", 'r') as pw_file:
            pw = pw_file.read()
        if a == pw:
            print("WELCOME SIR! PLEASE SPEAK [WAKE UP] TO LOAD ME UP")
            break
        elif i == 2 and a != pw:
            exit()
        else:
            print("Try again!!")

    # Intro GIF
    from Intro import play_gif
    play_gif()

    speak("Friday activated. Say wake up to start.")
    
    while True:
        query = takeCommand()
        if query == "none":
            continue

        # Activation
        if "wake up" in query:
            speak("Hello sir! I am ready to help you.")
            greetMe()
            
            while True:
                query = takeCommand()
                if query == "none":
                    continue

                # ------------------ Conversations ------------------
                if "hello" in query:
                    speak("Hello sir, how are you?")
                elif "i am fine" in query or "i'm fine" in query:
                    speak("That's great to hear, sir!")
                elif "how are you" in query:
                    speak("I'm doing great, sir! Always ready to help you.")
                elif "thank you" in query or "thanks" in query:
                    speak("You're welcome, sir!")
                elif "good morning" in query:
                    speak("Good morning, sir! Have a great day ahead.")
                elif "good afternoon" in query:
                    speak("Good afternoon, sir! How is your day going so far?")
                elif "good evening" in query:
                    speak("Good evening, sir! How was your day?")
                elif "good night" in query:
                    speak("Good night, sir! Sleep well and take care.")
                elif "who are you" in query:
                    speak("I am Friday, your personal desktop assistant, sir.")
                elif "what can you do" in query:
                    speak("I can perform many tasks, sir — from calculations to opening apps, fetching news, and much more.")
                elif "exit" in query or "go to sleep" in query:
                    speak("Ok sir, you can call me anytime.")
                    sys.exit(0)

                # ------------------ App Controls ------------------
                elif "open" in query:
                    query = query.replace("open", "").replace("friday", "")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")

                elif "close" in query:
                    query = query.replace("close", "").replace("friday", "")
                    speak(f"Closing {query} sir.")
                    pyautogui.hotkey("alt", "f4")

                # ------------------ Web Searches ------------------
                elif "google" in query:
                    searchGoogle(query)
                elif "youtube" in query:
                    searchYouTube(query)
                elif "wikipedia" in query:
                    searchWikipedia(query)

                # ------------------ Tools ------------------
                elif "calculate" in query:
                    query = query.replace("friday", "").replace("calculate", "")
                    Calc(query)
                elif "translate" in query:
                    query = query.replace("friday", "").replace("translate", "")
                    translategl(query)
                elif "set an alarm" in query:
                    handle_alarm()
                elif "stop the alarm" in query:
                    stop_alarm()
                    speak("Alarm stopped, sir.")
                elif "focus mode" in query:
                    speak("Entering focus mode....")
                    import subprocess
                    script_path = r"C:\Users\ASUS\OneDrive\Attachments\Desktop\Fri-Day\FocusMode.py"
                    subprocess.run(["powershell", "-Command", f'Start-Process python "{script_path}" -Verb runAs'])
                elif "show my focus graph" in query:
                    focus_graph()
                elif "send whatsapp message" in query:
                    sendMessage()
                elif "temperature" in query or "weather" in query:
                    get_weather_data(query, speak)
                elif "play a game" in query:
                    game_play()
                elif "news" in query:
                    latestNews(speak)
                elif "internet speed" in query:
                    download, upload = getSpeed()
                    speak(f"Your download speed is {download:.2f} Mbps and upload speed is {upload:.2f} Mbps")
                elif "score" in query or "cricket" in query:
                    speak("Fetching cricket updates, sir. Please wait.")
                    live_cricket_score_interactive()
                elif "screenshot" in query:
                    speak("Taking screenshot, sir.")
                    path = take_screenshot()
                    speak(f"Screenshot saved at {path}")

                # ------------------ Music ------------------
                elif "tired" in query:
                    speak("Playing your favourite songs, sir!")
                    songs = [
                        "https://www.youtube.com/watch?v=K9R7KcaettM",
                        "https://www.youtube.com/watch?v=-YlmnPh-6rE",
                        "https://www.youtube.com/watch?v=5GCfYLguTIs",
                        "https://www.youtube.com/watch?v=Z8IRRphKFZA"
                    ]
                    webbrowser.open(random.choice(songs))

                # ------------------ Misc ------------------
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that", "").replace("friday", "")
                    speak("You told me that " + rememberMessage)
                    with open("remember.txt", "a") as remember:
                        remember.write(rememberMessage + "\n")
                elif "what do you remember" in query:
                    with open("remember.txt", "r") as remember:
                        speak("You told me to remember: " + remember.read())

                elif "shutdown system" in query:
                    speak("Are you sure sir?")
                    shutdown = input("Do you wish to shutdown the system? (yes/no): ")
                    if shutdown.lower() == "yes":
                        os.system("shutdown /s /t 1")

                else:
                    speak("I am listening, sir. Please repeat the command.")

if __name__ == "__main__":
    main()
