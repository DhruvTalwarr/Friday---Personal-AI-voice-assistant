import pywhatkit
import pyttsx3
import speech_recognition 
import webbrowser
from bs4 import BeautifulSoup
import datetime
from time import sleep
import os
from datetime import timedelta
from datetime import datetime

# def speak(audio):
#     # print("=====Friday not activated yet=====\n")
#     engine = pyttsx3.init("sapi5")
#     voices = engine.getProperty("voices")
#     engine.setProperty("voice", voices[2].id) # Make SURE this index is correct
#     engine.setProperty("rate", 170)
#     print(f"Friday: {audio}") 
#     engine.say(audio)
#     engine.runAndWait()
    
#     # VERY IMPORTANT: Stop/Quit the engine to free up the SAPI resource
#     engine.stop() 
#     del engine 
from speak import speak, stop_speaking

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

update = int((datetime.now()+timedelta(minutes = 2)).strftime("%M"))
strTime = int(datetime.now().strftime("%H"))

def sendMessage():
    speak("Who do you want to message?")
    print(('''Yourself - 1\nMummy - 2\nPapa - 3'''))
    a= int(input("Enter your choice: "))
    if a == 1:
        speak("What is the message?")
        message = str(input("Enter the message: "))
        pywhatkit.sendwhatmsg("+919198697798", message, time_hour = strTime, time_min=update)
    elif a == 2:
        speak("What is the message?")
        message = str(input("Enter the message: "))
        pywhatkit.sendwhatmsg("+918318668926", message, time_hour = strTime, time_min=update)
    elif a == 3:
        speak("What is the message?")
        message = str(input("Enter the message: "))
        pywhatkit.sendwhatmsg("+919956803819", message, time_hour = strTime, time_min=update)
    else:
        speak("I am sorry sir, I am not able to find this contact")