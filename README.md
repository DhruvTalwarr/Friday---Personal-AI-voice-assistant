# 🤖 Friday: Your Personal AI Desktop Assistant

Project Friday is a comprehensive, voice-controlled desktop assistant built primarily in Python. It automates daily tasks, manages focus time, provides real-time information, and offers interactive utilities—all through simple voice commands.

---

## ✨ Features

Friday is engineered to be a powerful, multi-functional helper covering utility, communication, information retrieval, and productivity.

- **🎙️ Voice Control & Communication:** Full text-to-speech (pyttsx3) and command recognition for a hands-free experience.
- **⏰ Task & Time Management:** Set alarms, manage a task list, and schedule dedicated focus sessions.
- **🌐 Real-Time Information:** Check live weather, news headlines, cricket scores, and measure internet speed instantly.
- **🔍 Automated Searching:** Quickly perform searches on Google, YouTube, and Wikipedia.
- **💬 Utilities:** Automated WhatsApp messaging, real-time language translation, and a built-in calculator.
- **💾 Persistent Memory:** Save notes, passwords, and task lists locally for long-term usage.

---

## 🚀 Getting Started

These instructions will help you set up Project Friday on your local machine for development and testing.

### Prerequisites

- Python 3.x installed on your system.
- System-level dependencies for `pyttsx3` (PortAudio or audio playback libraries).

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/YourUsername/Project-Friday.git
   cd Project-Friday

2. **Install Dependencies**:

pip install -r requirements.txt

3. **Setup Configuration**:

Many modules (e.g., WeatherNow.py, translate.py) require API keys (OpenWeatherMap, Google Translate, etc.).

Update credential files:

password → securely store login tokens or keys.

AlarmText, AlarmTime, remember, task → set up initial data.


## 📂 Module Breakdown

### 1. Core Logic & Setup

| File / Module   | Description |
|-----------------|-------------|
| `friday_main.py` | Central command loop: initializes systems, handles voice input, maps commands, and manages workflow. |
| `installer`     | Utility for setting up environment or dependencies. |
| `speaker.py`    | Handles Text-to-Speech (TTS) using `pyttsx3`. |
| `GreetMe.py`    | Executes time-based, personalized voice greetings. |
| `Intro.py`      | Plays animated startup GIF (`dr strange.gif`) on launch. |

---

### 2. Information Retrieval

| File / Module           | Description |
|-------------------------|-------------|
| `SearchNow.py`          | Automates and speaks results from Google, YouTube, and Wikipedia searches. |
| `WeatherNow.py`         | Fetches and reports live weather updates via API. |
| `News.py`               | Retrieves and reads latest news headlines. |
| `live_cricket_score.py` | Fetches and reports live cricket match scores. |
| `test_speed.py`         | Measures and reports internet upload/download speed. |

---

### 3. Productivity & Utilities

| File / Module  | Description |
|----------------|-------------|
| `FocusMode.py`    | Starts a distraction-free focus session with timer. |
| `FocusGraph.py`   | Generates visual graphs of focus session performance. |
| `AlarmSet.py`     | Schedules and manages multiple alarms. |
| `Whatsapp.py`     | Sends automated WhatsApp messages (`pywhatkit` required). |
| `translate.py`    | Performs real-time text translations via API. |
| `keyboard.py`     | Handles input automation (volume control, shortcuts, screenshots). |
| `calulator`       | Simple module for mathematical calculations. |

---

### 4. Data & Assets

| File / Module                     | Purpose |
|-----------------------------------|---------|
| `requirements.txt`                | Lists all required Python libraries (requests, pyttsx3, speedtest). |
| `remember`                        | Stores assistant's long-term memory (notes, facts, preferences). |
| `task`                            | Manages user's to-do list or tasks. |
| `password`                         | Stores API keys and sensitive credentials (secure file permissions recommended). |
| `PyWhatKit_DB`                     | Database/log for WhatsApp message history or config. |
| `dr strange.gif`                   | Animation played on startup. |
| `soft_morning_alarm.mp3`           | Alarm sound file. |
| `dr strange-magic-circle-shield-sound.mp3` | Launch/activation sound effect. |

5. Development & Temporary Files
   
Temporary files used for testing/development:

alarm_temp.py, calc_module_temp.py, test_voice_temp.py, voices_temp.py

AlarmText, AlarmTime (temp configuration storage)

screenshot.png (example screenshot)

These files can generally be ignored for production or version control.

