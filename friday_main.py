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
import webbrowser

# # --- API CONFIGURATION ---
# API_KEY = "35e4afc4ee31a5903eff497df13d828b"
# BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
# CITY_NAME = "Kanpur, IN"

def speak(audio):
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
    
    print("---Task Completed---\n") 


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:

        print("\nListening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def alarm(query):
    timehere = open("AlarmTime.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

#main funtion
if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        #for activation
        if "wake up" in query:
            print("=====Friday Activated=====\n")
            greetMe()
            while True:
                query = takeCommand().lower()
                #normal convo
                if "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")
                #for breaking the loop
                elif "exit" in query or "stop" in query:
                    speak("Ok sir , You can me call anytime")
                    exit()
                
                #opeining and closing apps
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeapp
                    closeapp(query)

                #general tasks
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYouTube
                    searchYouTube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                #set an alarm
                elif "set an alarm" in query:
                    from AlarmSet import set_alarm_with_reminder
                    set_alarm_with_reminder(query, takeCommand)

                #temperature and weather automation 
                elif "temperature" in query or "weather" in query:
                    get_weather_data(query, speak)

                #setting an alarm
                # elif "set an alarm" in query:
                #     print("Input time example :- 10 and 10 and 10 ")
                #     speak("Set the time, sir")
                #     a =input("Please tell time :-")
                #     alarm(a)
                #     speak("Done sir")
                
                #automate youtube
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

                #remember
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that" "")
                    rememberMessage = query.replace("jarvis" "")
                    speak("You told me that" +rememberMessage)
                    remember = open("remember.txt", "a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("remember.txt" , "r")
                    speak("You told me to remember that" + remember.read())                

                    #make our own playlist
                elif "tired" in query:
                    speak("Playing your favourite songs, sir!")
                    a = (1, 2, 3)
                    b = random.choice(a)
                    if(b == 1):
                        webbrowser.open("https://www.youtube.com/watch?v=K9R7KcaettM")
                    elif(b == 2):
                        webbrowser.open("https://www.youtube.com/watch?v=-YlmnPh-6rE")
                    else:
                        webbrowser.open("https://www.youtube.com/watch?v=Z8IRRphKFZA")