# 🤖 Friday Voice Assistant

Friday is a Python-based desktop voice assistant designed to handle common tasks such as web searching, playing media, fetching real-time weather, and setting non-blocking alarms. It is built to be modular, making it easy to extend and maintain.

## 🚀 Getting Started

### Prerequisites

1.  **Python 3.x:** Ensure you have a recent version of Python installed (Python 3.8+ is recommended).
2.  **API Key:** A free API key from **OpenWeatherMap** is required for weather functionality. Replace the placeholder in `WeatherNow.py` with your key.

### Installation

Install the required Python libraries using pip:

pip install pyttsx3 SpeechRecognition requests pywhatkit wikipedia playsound


##**Running the Assistant**
Execute the main script from your terminal:

python friday_main.py

The assistant will initialize (Friday activated.) and wait for your command.

**📂 Project Structure and File Breakdown**

**File Name	Type	Description**
friday_main.py	Main File	The core execution file. It initializes the speech engine, runs the main listening loop, and manages the logic flow between commands and modules.
AlarmSet.py	Module	Contains the logic for setting the non-blocking alarm. It prompts the user for a time, calculates the delay, and plays the audio file (soft_morning_alarm.mp3) using a background thread.
WeatherNow.py	Module	Handles real-time weather and temperature queries. It constructs the API call to OpenWeatherMap and processes the JSON response.
SearchNow.py	Module	Handles external searches (Google, YouTube, and Wikipedia). It uses pywhatkit, webbrowser, and the wikipedia library to perform actions and fetch summaries.
GreetMe.py	Module	Contains the function to greet the user, typically based on the current time of day (Good Morning, Good Evening, etc.).
soft_morning_alarm.mp3	Audio File	The sound file played when the alarm set via AlarmSet.py is triggered.
Dictapp	Python Source	(Based on name) Likely a custom module for dictionary/definition lookups or potentially handling basic dictation/typing tasks.
keyboard	Python Source	(Based on name) Likely contains functions for simulating key presses or desktop automation, possibly used for system control or hotkeys.
_pycache_	Folder	Temporary Python cache folder. Generated automatically by Python for faster module loading.
Alarmtext	Text Document	(Temporary/Configuration) Likely a configuration file or a temporary file related to initial alarm testing.
AlarmTime	Python Source	(Temporary) Likely an older or test version of the logic now fully integrated into AlarmSet.py.
alarm_temp	Python Source	(Temporary) Test file used for initial alarm development.
test_voice_temp	Python Source	(Temporary) Test file used for checking voice input/output configurations.
voices_temp	Python Source	(Temporary) Test file used for configuring and selecting the correct pyttsx3 voice.
remember	Text Document	(Temporary) May have been used to test persistent memory or "remember" a piece of information.
installer	Python Source	(Temporary) A simple script used to install project dependencies.
