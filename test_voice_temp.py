import pyttsx3
import time

# Initialize the engine once
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

# Set voice to index 2 (or try index 0 for a simple test)
engine.setProperty("voice", voices[2].id) 
engine.setProperty("rate", 170)

# Speak a test phrase
print("Attempting to speak test phrase...")
engine.say("Hello. I am speaking without the microphone enabled.")
engine.runAndWait()

# Clean up
engine.stop()
print("Speech attempt complete.")