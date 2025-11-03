import pyttsx3
import speech_recognition
from GreetMe import greetMe
import requests
from bs4 import BeautifulSoup
from WeatherNow import get_weather_data
import datetime
import time
import os
import sys
import pyautogui
import keyboard
import random
from SearchNow import searchGoogle, searchYouTube, searchWikipedia
from AlarmSet import set_alarm_with_ring, stop_alarm
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
from live_cricket_score import live_cricket_score_interactive
from speak import speak, stop_speaking
from VoiceTyping import voice_typing_mode
from SwitchTab import switch_tab, switch_app, focus_app, switch_to_tab_number, close_tab, reopen_closed_tab, show_desktop, maximize_window, minimize_window
from open_new_tab import open_new_tab
from brightness import brightness_control
from CleanCodeExplainerGemini import explain_code_via_gemini

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


#Intro GIF
from Intro import play_gif
play_gif()


#take command function
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


#handle alarm function
def handle_alarm():
    try:
        set_alarm_with_ring(speak, takeCommand)
    except Exception as e:
        speak("Sorry sir, there was an error setting the alarm.")
        print(f"Alarm Error: {e}")


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

                if "hello" in query:
                    speak("Hello sir, how are you?")

                elif "i am fine" in query or "i'm fine" in query:
                    speak("That's great to hear, sir!")

                elif "how are you" in query:
                    speak("I'm doing great, sir! Always ready to help you.")

                elif "thank you" in query or "thanks" in query:
                    speak("You're most welcome, sir!")

                elif "good morning" in query:
                    speak("Good morning, sir! Hope your day starts with a smile.")

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

                elif "what's your name" in query or "your name" in query:
                    speak("My name is Friday, sir. Your virtual companion.")

                elif "who made you" in query or "who created you" in query:
                    speak("I was created by Dhruv Talwar, sir!")

                elif "nice" in query or "great" in query or "awesome" in query:
                    speak("Thank you, sir! Glad you liked it.")

                elif "are you there" in query:
                    speak("Always here for you, sir!")

                elif "i love you" in query:
                    speak("That's sweet of you, sir! But my heart belongs to the code.")

                elif "what's up" in query or "how's it going" in query:
                    speak("All good here, sir! Just waiting for your next command.")

                elif "exit" in query or "go to sleep" in query:
                    speak("Ok sir, you can call me anytime.")

                    # Stop pyttsx3 engine cleanly
                    try:
                        engine = pyttsx3.init("sapi5")
                        engine.stop()
                        del engine
                    except:
                        pass
                    sys.exit(0)



                #focus mode
                elif "focus mode" in query:
                    a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO ]: "))
                    if a == 1:
                        speak("Entering the focus mode....")

                        import subprocess
                        script_path = r"C:\Users\ASUS\OneDrive\Attachments\Desktop\Fri-Day\FocusMode.py"

                        # Run it as admin properly
                        subprocess.run(["powershell", "-Command", f'Start-Process python "{script_path}" -Verb runAs'])

                    else:
                        pass

                elif "show my focus graph" in query:
                    focus_graph()

                #switching tabs between browser
                elif "next tab" in query:
                    speak("Switching to next tab, sir.")
                    switch_tab("next")


                elif "previous tab" in query or "back tab" in query:
                    speak("Switching to previous tab, sir.")
                    switch_tab("previous")

                
                #switching between apps and windows
                elif "switch window" in query or "next window" in query:
                    speak("Switching to next window, sir.")
                    switch_app()

                #switching directly to a specific app
                elif "switch to" in query:
                    app_name = query.replace("switch to", "").strip()
                    focus_app(app_name) 


                #open new tab
                elif "open new tab" in query or "new tab" in query:
                    open_new_tab()

                

                elif "go to tab" in query or "switch to tab" in query:
                    words = query.split()
                    for word in words:
                        if word.isdigit():
                            tab_num = int(word)
                            switch_to_tab_number(tab_num)
                            break
                    else:
                        speak("Please say a tab number between one and nine.")

                elif "close this tab" in query or "close tab" in query:
                    # speak("Closing the current tab, sir.")
                    close_tab()

                elif "reopen closed tab" in query or "restore tab" in query:
                    # speak("Reopening last closed tab, sir.")
                    reopen_closed_tab()

                elif "show desktop" in query or "go to desktop" in query:
                    show_desktop()

                elif "minimize window" in query or "minimize this" in query or "minimise window" in query or "minimise this" in query:
                    minimize_window()

                elif "maximize window" in query or "maximize this" in query or "maximise window" in query or "maximise this" in query:
                    maximize_window()

                # Translation
                elif "translate" in query:
                    query = query.replace("friday", "").replace("translate", "").strip()
                    translategl(query)


                # Open any app
                elif "open" in query:
                    query = query.replace("open", "").replace("friday", "")
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
                    handle_alarm()

                elif "stop the alarm" in query:
                    stop_alarm()
                    speak("Alarm stopped, sir.")


                # Weather and Temperature
                elif "temperature" in query or "weather" in query:
                    get_weather_data(query, speak)


                # YouTube automation
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused, sir!")

                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played, sir!")

                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted, sir!")
                
                elif "unmute" in query:
                    pyautogui.press("m")
                    speak("video unmuted, sir!")

                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up, sir!")
                    volumeup()

                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir!")
                    volumedown()


                # Remember and Recall
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


                # Schedule my day
                elif "schedule my day" in query:
                    tasks = []
                    # Ask via speech
                    speak("Do you want to clear old tasks, sir? Please say yes or no.")
                    confirm = takeCommand().lower()
                    # Clear old tasks if user says yes
                    if "yes" in confirm:
                        open("tasks.txt", "w").close()
                        speak("Old tasks cleared successfully, sir.")
                    else:
                        speak("Keeping old tasks, sir.")
                    # Manual input for number of tasks
                    try:
                        no_tasks = int(input("Enter the number of tasks: "))
                    except ValueError:
                        speak("Invalid input, sir. Please enter a number next time.")
                        no_tasks = 0

                    # Manual input for each task
                    for i in range(no_tasks):
                        task = input(f"Enter task {i + 1}: ")
                        tasks.append(task)
                        with open("tasks.txt", "a") as file:
                            file.write(f"{i + 1}. {task}\n")

                    if tasks:
                        speak(f"Your {len(tasks)} tasks have been added successfully, sir.")
                    else:
                        speak("No new tasks were added, sir.")


                # Internet speed
                elif "internet speed" in query:
                    print("Checking internet speed...")
                    download, upload = getSpeed()
                    print(f"Download Speed: {download:.2f} Mbps")
                    print(f"Upload Speed: {upload:.2f} Mbps")
                    speak(f"Your download speed is {download:.2f} megabits per second")
                    speak(f"Your upload speed is {upload:.2f} megabits per second")


                #cricket score
                elif "score" in query or "cricket" in query:
                    speak("Fetching cricket updates, sir. Please wait.")
                    live_cricket_score_interactive()


                # Screenshot
                elif "screenshot" in query:
                    speak("Taking screenshot, sir.")
                    path = take_screenshot()
                    speak(f"Screenshot saved successfully at {path}")
                    speak("Here is the scoreboard, sir.")


                # Take photo
                elif "click my photo" in query:
                    speak("Taking your photo, sir.")
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("Say cheese in 3 seconds!")
                    pyautogui.press("enter")


                #voice typing mode
                elif "start typing" in query or "voice typing" in query:
                    voice_typing_mode()

                #brightness of system
                elif "brightness" in query:
                    brightness_control()


                # --- Code Explanation ---
                elif "explain this code" in query or "explain code" in query:
                    speak("Sure sir, please paste the code you want me to explain.")
                    print("Paste your code below. Type 'END' on a new line to finish:")

                    # Multi-line input until user types 'END'
                    user_code_lines = []
                    while True:
                        line = input()
                        if line.strip().upper() == "END":
                            break
                        user_code_lines.append(line)
                    
                    user_code = "\n".join(user_code_lines)

                    if not user_code.strip():
                        speak("No code was provided, sir. Returning to normal mode.")
                        continue

                    # Ask for programming language
                    speak("Which programming language is this code in, sir?")
                    lang = input("Enter language (e.g., Python, C++, Java): ").strip()
                    if not lang:
                        lang = "Python"  # Default to Python if not provided

                    # Call the CleanCodeExplainer
                    explain_code_via_gemini(user_code, language=lang)



        elif "exit" in query or "quit" in query:
            speak("Ok sir, you can call me anytime.")

            # Stop pyttsx3 engine cleanly
            try:
                engine = pyttsx3.init("sapi5")
                engine.stop()
                del engine
            except:
                pass
            sys.exit(0)