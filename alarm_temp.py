import pyttsx3
import datetime
import time
import os

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

extractedtime = open("AlarmTime.txt","r")
time = extractedtime.read()
Time = str(time)
extractedtime.close()

deletetime = open("AlarmTime.txt","r+")
deletetime.truncate(0)
deletetime.close()

def ring(time):
    timeset = str(time)
    timenow = timeset.replace("set alarm for","")
    timenow = timenow.replace("set alarm","")
    timenow = timenow.replace("for","")
    timenow = timenow.replace("to","")
    timenow = timenow.replace("friday","")
    timenow = timenow.replace(" and ",":")
    timenow = timenow.replace("at","")
    timenow = timenow.replace("a m","AM")
    timenow = timenow.replace("p m","PM")
    Alarmtime = str(timenow)
    print(Alarmtime)
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime == Alarmtime:
            speak("Alarm ringing, sir")
            os.startfile("soft_morning_alarm.mp3")

        elif currenttime + "00:00:30" == Alarmtime:
            exit()

ring(time)
