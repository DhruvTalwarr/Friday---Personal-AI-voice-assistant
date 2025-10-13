# 🤖 Friday Voice Assistant

Friday is a Python-based desktop voice assistant designed to handle common tasks such as web searching, playing media, fetching real-time weather, and setting non-blocking alarms. It is built to be modular, making it easy to extend and maintain.

## 🚀 Getting Started

### Prerequisites

1.  **Python 3.x:** Ensure you have a recent version of Python installed (Python 3.8+ is recommended).
2.  **API Key:** A free API key from **OpenWeatherMap** is required for weather functionality. Replace the placeholder in `WeatherNow.py` with your key.

### Installation

Install the required Python libraries using pip:

pip install pyttsx3 SpeechRecognition requests pywhatkit wikipedia playsound


**Running the Assistant**
Execute the main script from your terminal:

python friday_main.py

The assistant will initialize (Friday activated.) and wait for your command.

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

