import pyttsx3
from googletrans import Translator, LANGUAGES

def speak(text):
    """Speak text using pyttsx3."""
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[2].id)  # adjust index if needed
    engine.setProperty("rate", 170)
    engine.setProperty("volume", 2.0)
    print(f"Friday: {text}")
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def translategl(query):
    """Translate text and speak it using pyttsx3."""
    speak("Sure sir")
    translator = Translator()

    # Print all languages with codes for easy selection
    print("\nAvailable Languages:\n")
    for code, name in LANGUAGES.items():
        print(f"{code} : {name}")
    print("\n")  # extra line for clarity

    speak("Choose the language in which you want to translate")
    b = input("To_Lang (code or name) :- ").lower()

    # Find language code
    lang_code = None
    for code, name in LANGUAGES.items():
        if name.lower() == b or code.lower() == b:
            lang_code = code
            break

    if not lang_code:
        speak("Sorry sir, this language is not supported.")
        return

    # Translate
    try:
        text_to_translate = translator.translate(query, src="auto", dest=lang_code)
        translated_text = text_to_translate.text
        print(f"\nTranslated Text ({lang_code} - {LANGUAGES[lang_code]}): {translated_text}\n")
        speak("Here is the translated version")
        speak(translated_text)
    except Exception as e:
        print(f"Error: {e}")
        speak("Unable to translate")
