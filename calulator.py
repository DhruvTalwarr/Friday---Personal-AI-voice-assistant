import wolframalpha
import pyttsx3
import speech_recognition as sr

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

def WolframAlpha(query):
    api_key = "YOUR_API_KEY"
    requester = wolframalpha.Client(api_key)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("I am sorry sir, I am not able to find the answer for this question")

def Calc(query):
    term = str(query)
    term = term.replace("calculate", "")
    term = term.replace("friday", "")
    term = term.replace("multiply", "*")
    term = term.replace("plus", "+")
    term = term.replace("minus", "-")
    term = term.replace("divide", "/")

    final = str(term)
    try:
        result = WolframAlpha(final)
        print(f"{result}")
        speak(result)
    except:

        speak("I am sorry sir, I am not able to calculate this")
