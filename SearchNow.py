import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser as wb
import requests 

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
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

from speak import speak, stop_speaking


# engine = pyttsx3.init("sapi5")
# voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[2].id) 


# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

def searchGoogle(query):
    if "google" in query:        
        query = query.replace("Friday", "")
        query = query.replace("google search", "")
        query = query.replace("google", "")
        
        speak("Searching Google for that query.")

        try:
            pywhatkit.search(query) 
            result = wikipedia.summary(query, sentences = 1)
            speak("Here is a brief summary:")
            speak(result)

        except wikipedia.exceptions.PageError:
            speak("I found the search results, but no direct summary was available.")
            
        except Exception as e:
            speak("Sorry, I could not complete the Google search and summary.")
            print(f"Google search error: {e}")

def searchYouTube(query):
    if "youtube" in query: 
        speak("This is what I found for your YouTube search.")
        query = query.replace("Friday", "")
        query = query.replace("youtube search", "")
        query = query.replace("youtube", "")
        
        web = "https://www.youtube.com/results?search_query=" + query
        wb.open(web)
        pywhatkit.playonyt(query)
        
        speak("Playing on YouTube now, sir.")

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching Wikipedia...")
        
        # Cleaning the query for search
        query = query.replace("wikipedia", "").replace("search", "").replace("friday", "").strip()
        
        try:
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        except requests.exceptions.ConnectionError as e:
            speak("I'm sorry sir, there was a temporary network error while connecting to Wikipedia. Please try the search again.")
            print(f"Wikipedia Connection Error: {e}")
            
        except wikipedia.exceptions.PageError:
            speak(f"Sorry sir, I couldn't find a Wikipedia page matching '{query}'.")

        except Exception as e:
            speak("An unexpected error occurred during the Wikipedia search.")
            print(f"General Wikipedia Error: {e}")
