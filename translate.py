import pyttsx3
from googletrans import Translator, LANGUAGES
from speak import speak, stop_speaking


def translategl(query):
    """Translate spoken text and read the translation aloud."""
    speak("Sure sir. Let's translate it.")
    translator = Translator()

    # Show all languages (for terminal users)
    print("\nAvailable Languages:\n")
    for code, name in LANGUAGES.items():
        print(f"{code} : {name}")
    print("\n")

    speak("Please tell me or type the language you want to translate into.")
    b = input("To_Lang (code or name) :- ").lower()

    # Find the correct language code
    lang_code = None
    for code, name in LANGUAGES.items():
        if b == code.lower() or b == name.lower():
            lang_code = code
            break

    if not lang_code:
        speak("Sorry sir, this language is not supported.")
        return

    try:
        # Perform translation
        translated = translator.translate(query, src="auto", dest=lang_code)
        translated_text = translated.text

        print(f"\nTranslated Text ({lang_code} - {LANGUAGES[lang_code]}): {translated_text}\n")
        speak(f"Here is the translation in {LANGUAGES[lang_code]}.")
        speak(translated_text)

    except Exception as e:
        print(f"Error: {e}")
        speak("Sorry sir, I was unable to translate that.")
