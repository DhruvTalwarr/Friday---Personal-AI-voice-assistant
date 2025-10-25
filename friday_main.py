import pyttsx3
import speech_recognition
from GreetMe import greetMe
import requests
from bs4 import BeautifulSoup
from WeatherNow import get_weather_data
import datetime
import time
import os
import pyautogui
import keyboard
import random
from SearchNow import searchGoogle, searchYouTube, searchWikipedia
from AlarmSet import set_alarm_with_ring
import webbrowser
from calulator import Calc, WolframAlpha
from News import latestNews
from Whatsapp import sendMessage
import speedtest
from test_speed import getSpeed
from plyer import notification
from live_cricket_score import live_cricket_score_interactive
from game import game_play
from keyboard import take_screenshot
from FocusGraph import focus_graph
from translate import translategl

# setting password of friday
for i in range(3):
    a = input("Enter password to open Friday: ")
    with open("password.txt", 'r') as pw_file:
        pw = pw_file.read()

    if a == pw:
        print("WELCOME SIR! PLEASE SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif i == 2 and a != pw:
        exit()
    elif a != pw:
        print("Try again!!")

from Intro import play_gif
play_gif()


def speak(audio):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[2].id)  # Adjust if invalid
    engine.setProperty('volume', 2.0)
    engine.setProperty("rate", 170)
    print(f"Friday: {audio}")
    engine.say(audio)
    engine.runAndWait()
    engine.stop()
    del engine


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
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
    return query


def alarm(query):
    with open("AlarmTime.txt", "a") as timehere:
        timehere.write(query)
    os.startfile("alarm.py")


# main function
if __name__ == "__main__":
    while True:
        query = takeCommand().lower()

        # Activation
        if "wake up" in query:
            print("=====Friday Activated=====\n")
            greetMe()

            while True:
                query = takeCommand().lower()

                # Normal conversation
                if "hello" in query:
                    speak("Hello sir, how are you ?")

                elif "i am fine" in query:
                    speak("that's great, sir")

                elif "how are you" in query:
                    speak("Perfect, sir")

                elif "thank you" in query:
                    speak("you are welcome, sir")

                elif "exit" in query or "stop" in query:
                    speak("Ok sir , You can me call anytime")
                    exit()

                # Focus mode
                elif "focus mode" in query:
                    a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO ]"))
                    if a == 1:
                        speak("Entering the focus mode....")
                        os.startfile("C:\\Users\\ASUS\\OneDrive\\Attachments\\Desktop\\Fri-Day\\FocusMode.py")
                    else:
                        pass

                elif "show my focus graph" in query:
                    focus_graph()

                # Translation
                elif "translate" in query:
                    query = query.replace("friday", "").replace("translate", "")
                    translategl(query)

                # Open any app
                elif "open" in query:
                    query = query.replace("open", "").replace("jarvis", "")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")

                # Close any app
                elif "close" in query:
                    query = query.replace("close", "").replace("friday", "").strip()
                    speak(f"Closing {query} sir.")
                    pyautogui.hotkey("alt", "f4")

                # Google, YouTube, Wikipedia search
                elif "google" in query:
                    searchGoogle(query)

                elif "youtube" in query:
                    searchYouTube(query)

                elif "wikipedia" in query:
                    searchWikipedia(query)

                # Game
                elif "play a game" in query:
                    game_play()

                # Alarm
                elif "set an alarm" in query:
                    set_alarm_with_ring(query, takeCommand)

                # Weather
                elif "temperature" in query or "weather" in query:
                    get_weather_data(query, speak)

                # YouTube automation
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")

                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")

                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")

                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up, sir!")
                    volumeup()

                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir!")
                    volumedown()

                # Remember
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that", "").replace("friday", "")
                    speak("You told me that " + rememberMessage)
                    with open("remember.txt", "a") as remember:
                        remember.write(rememberMessage)

                elif "what do you remember" in query:
                    with open("remember.txt", "r") as remember:
                        speak("You told me to remember that " + remember.read())

                # Music
                elif "tired" in query:
                    speak("Playing your favourite songs, sir!")
                    songs = [
                        "https://www.youtube.com/watch?v=K9R7KcaettM",
                        "https://www.youtube.com/watch?v=-YlmnPh-6rE",
                        "https://www.youtube.com/watch?v=5GCfYLguTIs",
                        "https://www.youtube.com/watch?v=Z8IRRphKFZA"
                    ]
                    webbrowser.open(random.choice(songs))

                # News
                elif "news" in query:
                    latestNews(speak)

                # Calculation
                elif "calculate" in query:
                    query = query.replace("friday", "").replace("calculate", "")
                    Calc(query)

                # WhatsApp message
                elif "send whatsapp message" in query:
                    sendMessage()

                # Shutdown system
                elif "shutdown system" in query:
                    speak("Are you sure sir?")
                    shutdown = input("Do you wish to shutdown the system? (yes/no): ")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")
                    elif shutdown == "no":
                        break

                # Change password
                elif "change password" in query:
                    speak("What's the new password?")
                    new_pw = input("Enter the new password: ")
                    with open("password.txt", 'w') as new_password:
                        new_password.write(new_pw)
                    speak("Done sir!")
                    speak(f"Your new password is: {new_pw}")

                # Schedule
                elif "schedule my day" in query:
                    tasks = []
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        open("tasks.txt", "w").close()
                    no_tasks = int(input("Enter the no. of tasks :- "))
                    for i in range(no_tasks):
                        task = input("Enter the task :- ")
                        tasks.append(task)
                        with open("tasks.txt", "a") as file:
                            file.write(f"{i}. {task}\n")

                # Internet speed
                elif "internet speed" in query:
                    print("Checking internet speed...")
                    download, upload = getSpeed()
                    print(f"Download Speed: {download:.2f} Mbps")
                    print(f"Upload Speed: {upload:.2f} Mbps")
                    speak(f"Your download speed is {download:.2f} megabits per second")
                    speak(f"Your upload speed is {upload:.2f} megabits per second")

                # Cricket score
                elif "score" in query or "cricket score" in query:
                    speak("Fetching live cricket matches, sir.")
                    live_cricket_score_interactive()
                    speak("Here is the scoreboard.")

                # Screenshot
                elif "screenshot" in query:
                    speak("Taking screenshot, sir.")
                    path = take_screenshot()
                    speak(f"Screenshot saved successfully at {path}")

                # Take photo
                elif "click my photo" in query:
                    speak("Taking your photo, sir.")
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("Say cheese in 3 seconds!")
                    pyautogui.press("enter")
