import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

print(f"Total voices loaded: {len(voices)}")
for i, voice in enumerate(voices):
    print(f"Index {i}: {voice.name}")