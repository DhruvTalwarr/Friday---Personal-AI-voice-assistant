import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print("Available voices:")
for i, v in enumerate(voices):
    print(i, v.name)

engine.setProperty('voice', voices[2].id)
engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)
engine.say("Hello, this is a test for Friday's voice system.")
engine.runAndWait()
