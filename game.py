import pyttsx3
import speech_recognition 
import random
from speak import speak, stop_speaking

# def speak(audio):
#     engine = pyttsx3.init("sapi5")
#     voices = engine.getProperty("voices")
#     engine.setProperty("voice", voices[2].id) # Make SURE this index is correct
#     engine.setProperty('volume', 2.0)
#     engine.setProperty("rate", 170)
#     print(f"Friday: {audio}") 
#     engine.say(audio)
#     engine.runAndWait()
    
#     # VERY IMPORTANT: Stop/Quit the engine to free up the SAPI resource
#     engine.stop() 
#     del engine 
    
    # print("---Task Completed---\n") 


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

def game_play():
    speak("Let's play Rock, Paper, Scissors!")
    print("Game Start! Best of 5 rounds.")
    i = 0
    me = 0
    friday = 0
    while(i < 3):
        choose = ('rock', 'paper', 'scissors')
        friday_choice = random.choice(choose)
        query = takeCommand().lower()
        if (query == "rock"):
            if(friday_choice == "rock"):
                speak("It's a tie! We both chose rock.")
                print(f"Score: You {me} - Friday {friday}")
            elif(friday_choice == "paper"):
                friday += 1
                speak("I win! Paper covers rock.")
                print(f"Score: You {me} - Friday {friday}")
            else:
                me += 1
                speak("You win! Rock crushes scissors.")
                print(f"Score: You {me} - Friday {friday}")
                
        elif (query == "paper"):
            if(friday_choice == "rock"):
                me += 1
                speak("You win! Paper covers rock.")
                print(f"Score: You {me} - Friday {friday}")
            elif(friday_choice == "paper"):
                speak("It's a tie! We both chose paper.")
                print(f"Score: You {me} - Friday {friday}")
            else:
                friday += 1
                speak("I win! Scissors cut paper.")
                print(f"Score: You {me} - Friday {friday}")

        elif (query == "scissors"):
            if(friday_choice == "rock"):
                friday += 1
                speak("I win! Rock crushes scissors.")
                print(f"Score: You {me} - Friday {friday}")
            elif(friday_choice == "paper"):
                me += 1
                speak("You win! Scissors cut paper.")
                print(f"Score: You {me} - Friday {friday}")
            else:
                speak("It's a tie! We both chose scissors.")
                print(f"Score: You {me} - Friday {friday}")
        
        else:
            speak("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        i += 1

    if(me > friday):
        speak(f"Congratulations! You won the game with a score of {me} to {friday}.")
    elif(friday > me):
        speak(f"I win the game with a score of {friday} to {me}. Better luck next time!")
    else:   
        speak(f"The game is a tie with both of us scoring {me}.")
