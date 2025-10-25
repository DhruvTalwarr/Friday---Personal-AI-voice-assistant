# import wolframalpha
import pyttsx3

def speak(audio):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[2].id)  # adjust index if needed
    engine.setProperty("rate", 170)
    print(f"Friday: {audio}")
    engine.say(audio)
    engine.runAndWait()
    engine.stop()
    del engine

# def WolframAlpha(query):
#     api_key = "29GG6A9GVP"  # ✅ Your AppID from WolframAlpha (Short Answers API)
#     requester = wolframalpha.Client(api_key)
#     try:
#         requested = requester.query(query)
#         answer = next(requested.results).text
#         return answer
#     except Exception as e:
#         print(f"⚠️ WolframAlpha Error: {e}")
#         speak("I am sorry sir, I couldn't find an answer to that question.")
#         return None

# def calculator(query):
#     term = str(query).lower()
#     term = term.replace("calculate", "")
#     term = term.replace("friday", "")
#     term = term.replace("multiply", "*")
#     term = term.replace("plus", "+")
#     term = term.replace("minus", "-")
#     term = term.replace("divide", "/")

#     final = term.strip()
#     print(f"🧮 Query to WolframAlpha: {final}")

#     result = WolframAlpha(final)
#     if result:
#         print(f"✅ Result: {result}")
#         speak(f"The answer is {result}")
#     else:
#         speak("I am sorry sir, I couldn't perform the calculation.")

import requests

def WolframAlpha(query):
    api_key = "29GG6A9GVP"  # Your Short Answers API key
    base_url = "https://api.wolframalpha.com/v1/result"
    params = {"i": query, "appid": api_key}

    try:
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            return response.text
        else:
            print(f"⚠️ WolframAlpha API Error: {response.status_code}")
            speak("I am sorry sir, I couldn't find an answer to that question.")
            return None
    except Exception as e:
        print(f"⚠️ Connection Error: {e}")
        speak("I am sorry sir, I couldn't connect to WolframAlpha.")
        return None



# calc_module.py

# import wolframalpha

# # 🔑 Replace this with your actual WolframAlpha App ID
# APP_ID = "29GG6A9GVP"

# def calculator(query):
#     """
#     Uses the WolframAlpha API to answer math or factual queries.
#     Example: '10 + 20', 'square root of 25', 'integrate x^2 dx'
#     """

#     try:
#         client = wolframalpha.Client(APP_ID)
#         res = client.query(query)
#         answer = next(res.results).text
#         return f"The answer is {answer}"

#     except StopIteration:
#         return "Sorry, I couldn't find an answer to that question."
#     except Exception as e:
#         return f"Sorry, an error occurred while calculating: {str(e)}"
