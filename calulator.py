
import wolframalpha
import pyttsx3
from speak import speak, stop_speaking

# def speak(audio):
#     engine = pyttsx3.init("sapi5")
#     voices = engine.getProperty("voices")
#     engine.setProperty("voice", voices[2].id)  # Change index if needed
#     engine.setProperty("rate", 170)
#     print(f"Friday: {audio}")
#     engine.say(audio)
#     engine.runAndWait()
#     engine.stop()


def WolframAlpha(query):
    api_key = "93KA8A8Q27"  # Your App ID
    try:
        requester = wolframalpha.Client(api_key)
        requested = requester.query(query)
        answer = next(requested.results).text
        return answer
    except StopIteration:
        return None
    except Exception as e:
        print(f"[Error: WolframAlpha failed] {e}")
        return None


def Calc(query):
    """Perform calculation using WolframAlpha, fallback to local eval."""
    term = str(query).lower()

    # Clean up query text
    replacements = {
        "calculate": "",
        "friday": "",
        "plus": "+",
        "minus": "-",
        "divide": "/",
        "divided by": "/",
        "multiply": "*",
        "multiplied by": "*",
        "x": "*",
        "into": "*",
        "power": "**"
    }
    for word, sym in replacements.items():
        term = term.replace(word, sym)

    final = term.strip()
    print(f"[DEBUG] Calculating: {final}")

    # Try WolframAlpha first
    result = WolframAlpha(final)

    if not result:
        # Fallback to local Python eval for basic math
        try:
            result = str(eval(final))
        except Exception as e:
            print(f"[Error: Local eval failed] {e}")
            result = None

    if result:
        print(f"Result: {result}")
        speak(f"The answer is {result}")
    else:
        speak("I am sorry sir, I am not able to calculate this.")
