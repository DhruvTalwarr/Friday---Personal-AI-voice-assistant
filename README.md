🤖 Friday Voice Assistant

Friday is a modular, Python-based desktop voice assistant capable of performing everyday tasks such as web searches, playing media, fetching real-time weather updates, and setting non-blocking alarms.
It’s designed with clean modular architecture — making it easy to extend, debug, and maintain.

🚀 Getting Started
🧩 Prerequisites

Before you begin, make sure you have the following installed:

Python 3.8 or higher
You can verify your Python version using:

python --version


OpenWeatherMap API Key

Sign up at OpenWeatherMap
 to get a free API key.

Replace the placeholder key inside WeatherNow.py with your actual key:

api_key = "YOUR_API_KEY"

⚙️ Installation

Clone this repository and install the dependencies:

git clone https://github.com/yourusername/friday-voice-assistant.git
cd friday-voice-assistant
pip install pyttsx3 SpeechRecognition requests pywhatkit wikipedia playsound

▶️ Running the Assistant

Once everything is set up, run the main file:

python friday_main.py


When started successfully, Friday will greet you and display:

Friday activated. Waiting for your command...


You can now start interacting with Friday using your voice commands. 🎤

💡 Example Commands

“What’s the weather like today?”

“Search Python programming on Google.”

“Play music on YouTube.”

“Set an alarm for 7 AM.”

“Who is Elon Musk?”


| **File Name**            | **Type**              | **Description**                                                                                                                                                          |
| ------------------------ | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `friday_main.py`         | 🧠 **Main File**      | The core execution file. It initializes the speech engine, runs the main listening loop, and manages the logic flow between commands and modules.                        |
| `AlarmSet.py`            | ⏰ **Module**          | Contains the logic for setting a non-blocking alarm. It prompts the user for a time, calculates the delay, and plays `soft_morning_alarm.mp3` using a background thread. |
| `WeatherNow.py`          | 🌦️ **Module**        | Handles real-time weather and temperature queries. It constructs the API call to OpenWeatherMap and processes the JSON response.                                         |
| `SearchNow.py`           | 🌐 **Module**         | Handles external searches (Google, YouTube, Wikipedia). It uses `pywhatkit`, `webbrowser`, and the `wikipedia` library to perform actions and fetch summaries.           |
| `GreetMe.py`             | 👋 **Module**         | Contains the function to greet the user based on the current time of day (e.g., Good Morning, Good Evening).                                                             |
| `soft_morning_alarm.mp3` | 🎵 **Audio File**     | The sound file played when the alarm set via `AlarmSet.py` is triggered.                                                                                                 |
| `Dictapp.py`             | 📘 **Python Source**  | Likely a custom module for dictionary/definition lookups or basic dictation/typing tasks.                                                                                |
| `keyboard.py`            | ⌨️ **Python Source**  | Likely contains functions for simulating key presses or desktop automation, possibly used for system control or hotkeys.                                                 |
| `__pycache__/`           | ⚙️ **Folder**         | Temporary Python cache folder. Generated automatically by Python for faster module loading.                                                                              |
| `Alarmtext.txt`          | 📝 **Text Document**  | A configuration or temporary file related to initial alarm testing.                                                                                                      |
| `AlarmTime.py`           | 🧩 **Python Source**  | A temporary or older version of the logic now fully integrated into `AlarmSet.py`.                                                                                       |
| `alarm_temp.py`          | 🧪 **Python Source**  | Test file used for initial alarm development.                                                                                                                            |
| `test_voice_temp.py`     | 🎙️ **Python Source** | Temporary test file used for checking voice input/output configurations.                                                                                                 |
| `voices_temp.py`         | 🗣️ **Python Source** | Temporary test file used for configuring and selecting the correct `pyttsx3` voice.                                                                                      |
| `remember.txt`           | 💾 **Text Document**  | Temporary file possibly used to test persistent memory or to "remember" specific user data.                                                                              |
| `installer.py`           | ⚡ **Python Source**   | Temporary script used to install or manage project dependencies.                                                                                                         |

