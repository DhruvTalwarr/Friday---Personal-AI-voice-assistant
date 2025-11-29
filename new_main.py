"""
friday_piper_ollama.py

Friday Desktop Assistant (cleaned & consolidated)
- Piper (local) for TTS
- Ollama (local) for chat/answers (http://localhost:11434)
- Preserves original assistant features with safer multitasking & LED handling
"""

# -----------------------
# Standard libraries
# -----------------------
import os
import re
import sys
import time
import subprocess
import winsound
import random
import threading
import datetime
from typing import Optional

# -----------------------
# Networking / parsing
# -----------------------
import requests
import json

# -----------------------
# Speech / Recognition / Automation
# -----------------------
try:
    import speech_recognition as sr
except Exception:
    sr = None
try:
    import pyautogui as pag
except Exception:
    pag = None
import webbrowser

# keyboard module (optional)
try:
    import keyboard
    # some custom helpers may exist in keyboard module in your project
    take_screenshot = getattr(keyboard, "take_screenshot", lambda: "screenshot_path_placeholder")
    volumeup = getattr(keyboard, "volumeup", lambda: None)
    volumedown = getattr(keyboard, "volumedown", lambda: None)
except Exception:
    keyboard = None
    take_screenshot = lambda: "screenshot_path_placeholder"
    volumeup = lambda: None
    volumedown = lambda: None

# -----------------------
# Optional local modules helper
# -----------------------
def _optional_import(name, attr=None):
    """
    Try to import module name. If attr is provided, return getattr(module, attr).
    On failure, return None.
    """
    try:
        mod = __import__(name)
        return getattr(mod, attr) if attr else mod
    except Exception:
        return None

# Load optional modules gracefully with safe defaults
GreetMe = _optional_import("GreetMe")
greetMe = getattr(GreetMe, "greetMe", lambda: print("greetMe() placeholder"))

WeatherNow = _optional_import("WeatherNow")
get_weather_data = getattr(WeatherNow, "get_weather_data", lambda q, s: s("Weather module not available") if callable(s) else None)

SearchNow = _optional_import("SearchNow")
searchGoogle = getattr(SearchNow, "searchGoogle", lambda q: print("searchGoogle placeholder"))
searchYouTube = getattr(SearchNow, "searchYouTube", lambda q: print("searchYouTube placeholder"))
searchWikipedia = getattr(SearchNow, "searchWikipedia", lambda q: print("searchWikipedia placeholder"))

AlarmSet = _optional_import("AlarmSet")
set_alarm_with_ring = getattr(AlarmSet, "set_alarm_with_ring", lambda s, t: print("set_alarm placeholder"))
stop_alarm = getattr(AlarmSet, "stop_alarm", lambda: print("stop_alarm placeholder"))

News = _optional_import("News")
latestNews = getattr(News, "latestNews", lambda s: s("News module not available") if callable(s) else None)

Whatsapp = _optional_import("Whatsapp")
sendMessage = getattr(Whatsapp, "sendMessage", lambda: print("sendMessage placeholder"))

test_speed = _optional_import("test_speed")
getSpeed = getattr(test_speed, "getSpeed", lambda: (0.0, 0.0))

live_cricket_score = _optional_import("live_cricket_score")
live_cricket_score_interactive = getattr(live_cricket_score, "live_cricket_score_interactive", lambda: print("cricket placeholder"))

game = _optional_import("game")
game_play = getattr(game, "game_play", lambda: print("game placeholder"))

FocusGraph = _optional_import("FocusGraph")
focus_graph = getattr(FocusGraph, "focus_graph", lambda: print("focus_graph placeholder"))

translate_mod = _optional_import("translate")
translategl = getattr(translate_mod, "translategl", lambda q: print("translate placeholder"))

VoiceTyping = _optional_import("VoiceTyping")
voice_typing_mode = getattr(VoiceTyping, "voice_typing_mode", lambda: print("voice typing placeholder"))

arduino_mod = _optional_import("arduino_control")
led_on = getattr(arduino_mod, "led_on", lambda x: print(f"led_on({x}) placeholder"))
led_off = getattr(arduino_mod, "led_off", lambda: print("led_off() placeholder"))

SwitchTab = _optional_import("SwitchTab")
switch_tab = getattr(SwitchTab, "switch_tab", lambda x: print("switch_tab placeholder"))
switch_app = getattr(SwitchTab, "switch_app", lambda: print("switch_app placeholder"))
focus_app = getattr(SwitchTab, "focus_app", lambda x: print("focus_app placeholder"))
switch_to_tab_number = getattr(SwitchTab, "switch_to_tab_number", lambda n: print("switch_to_tab_number placeholder"))
close_tab = getattr(SwitchTab, "close_tab", lambda: print("close_tab placeholder"))
reopen_closed_tab = getattr(SwitchTab, "reopen_closed_tab", lambda: print("reopen_closed_tab placeholder"))
show_desktop = getattr(SwitchTab, "show_desktop", lambda: print("show_desktop placeholder"))
maximize_window = getattr(SwitchTab, "maximize_window", lambda: print("maximize_window placeholder"))
minimize_window = getattr(SwitchTab, "minimize_window", lambda: print("minimize_window placeholder"))

open_new_tab_mod = _optional_import("open_new_tab")
open_new_tab = getattr(open_new_tab_mod, "open_new_tab", lambda: print("open_new_tab placeholder"))

brightness_mod = _optional_import("brightness")
brightness_control = getattr(brightness_mod, "brightness_control", lambda: print("brightness placeholder"))

CleanCodeExplainer = _optional_import("CleanCodeExplainerGemini")
explain_code_via_gemini = getattr(CleanCodeExplainer, "explain_code_via_gemini", lambda code, language="Python": print("explain_code placeholder"))

call_handler = _optional_import("call_handler")
pick_call = getattr(call_handler, "pick_call", lambda: print("pick_call placeholder"))
reject_call = getattr(call_handler, "reject_call", lambda: print("reject_call placeholder"))

Wp = _optional_import("Wp")
send_whatsapp_desktop = getattr(Wp, "send_whatsapp_desktop", lambda: print("send_whatsapp_desktop placeholder"))

pdf_explain = _optional_import("pdf_explain")
read_pdf = getattr(pdf_explain, "read_pdf", lambda p: "")
read_docx = getattr(pdf_explain, "read_docx", lambda p: "")
summarize_text = getattr(pdf_explain, "summarize_text", lambda t: "Summary placeholder")

email_summarizer = _optional_import("email_summarizer")
clean_email_html = getattr(email_summarizer, "clean_email_html", lambda x: x)
summarize_email = getattr(email_summarizer, "summarize_email", lambda x: "Email summary placeholder")

Intro = _optional_import("Intro")
play_gif = getattr(Intro, "play_gif", lambda: None)

# -----------------------
# Piper TTS configuration (update your local paths)
# -----------------------
PIPER_EXE = r"C:\Users\ASUS\OneDrive\Attachments\Desktop\Fri-Day\piper\piper.exe"   # update if needed
MODEL_PATH = r"C:\Users\ASUS\OneDrive\Attachments\Desktop\Fri-Day\voice\en_US-kusal-medium.onnx"  # update if needed
TEMP_WAV = os.path.join(os.path.expanduser("~"), "friday_tts_out.wav")

if not os.path.exists(PIPER_EXE):
    print(f"Warning: piper executable not found at {PIPER_EXE}. Update PIPER_EXE.")
if not os.path.exists(MODEL_PATH):
    print(f"Warning: Piper model not found at {MODEL_PATH}. Update MODEL_PATH.")

# -----------------------
# Reusable Piper TTS functions
# -----------------------
def _generate_tts_wav(text: str, timeout: int = 20) -> Optional[str]:
    if not text:
        return None
    try:
        proc = subprocess.Popen(
            [PIPER_EXE, "--model", MODEL_PATH, "--output_file", TEMP_WAV],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
    except FileNotFoundError:
        print("Piper executable not found. Check PIPER_EXE.")
        return None
    except Exception as e:
        print("Failed to start Piper:", e)
        return None

    try:
        proc.communicate(input=text, timeout=timeout)
    except subprocess.TimeoutExpired:
        proc.kill()
        print("Piper TTS generation timed out.")
        return None
    except Exception as e:
        print("Piper generation error:", e)
        return None

    return TEMP_WAV if os.path.exists(TEMP_WAV) else None


def speak(text: str):
    """Generate TTS and play asynchronously."""
    if not text:
        return
    print("FRIDAY:", text)
    wav = _generate_tts_wav(text)
    if not wav:
        return
    try:
        winsound.PlaySound(wav, winsound.SND_FILENAME | winsound.SND_ASYNC)
    except Exception as e:
        print("Playback error:", e)


def stop_speaking():
    """Stop any ongoing Piper playback."""
    try:
        winsound.PlaySound(None, winsound.SND_ASYNC)
    except Exception:
        pass

# -----------------------
# Ollama chat (local)
# -----------------------
EXIT_COMMANDS = {"exit", "quit", "stop", "bye", "go to sleep", "exit friday", "quit friday", "stop friday", "bye friday", "go to sleep friday"}
FALLBACK_RESPONSES = [
    "Could you clarify that?",
    "I don't have an answer for that yet.",
    "Please ask something else.",
    "I'm learning — ask me another question."
]
MAX_OUTPUT_TOKENS = 120
MAX_CHARS_AFTER = 250

def _shorten_response(text: str, max_chars: int = MAX_CHARS_AFTER) -> str:
    text = (text or "").strip()
    if not text:
        return ""
    sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', text) if s.strip()]
    if sentences:
        short = '. '.join(sentences[:2])
        if not short.endswith(('.', '!', '?')):
            short = short + '.'
    else:
        short = text
    if len(short) > max_chars:
        return short[:max_chars].rstrip() + "..."
    return short

def ollama_chat(prompt: str, model: str = "phi3") -> str:
    prompt = (prompt or "").strip()
    if not prompt:
        return "Please say something so I can respond."

    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "max_output_tokens": MAX_OUTPUT_TOKENS
    }
    try:
        resp = requests.post(url, json=payload, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        text = data.get("response", "") or data.get("text", "") or ""
        text = _shorten_response(text)
        return text if text else random.choice(FALLBACK_RESPONSES)
    except Exception as e:
        print("Ollama error:", e)
        return random.choice(FALLBACK_RESPONSES)

# -----------------------
# Helper: safe phrase checks
# -----------------------
def phrase_contains_any(phrase: str, options):
    """Return True if any option appears exactly as a substring token sequence."""
    phrase = phrase.lower()
    for o in options:
        if o.lower() in phrase:
            return True
    return False

# -----------------------
# Single-task handler (improved safety)
# -----------------------
def handle_single_task(task: str):
    task = (task or "").strip().lower()
    if not task:
        return

    # Exact-ish mapped phrases for turning ON LEDs (safe)
    led_on_map = {
        3: ["turn on led a", "turn on led 3", "led 3 on", "light 3 on", "turn led 3 on"],
        5: ["turn on led b", "turn on led 5", "led 5 on", "light 5 on", "turn led 5 on"],
        7: ["turn on led c", "turn on led 7", "led 7 on", "light 7 on", "turn led 7 on"]
    }

    for pin, phrases in led_on_map.items():
        if any(p in task for p in phrases):
            try:
                led_on(pin)
            except Exception as e:
                print("led_on error:", e)
            speak(f"LED {pin} turned on.")
            return

    # SAFER LED-OFF (do not match 'led off' broadly)
    led_off_phrases = [
        "turn off leds",
        "turn off all leds",
        "all leds off",
        "switch off leds",
        "switch off all leds",
        "turn off lights",
        "switch off lights",
    ]
    if any(p in task for p in led_off_phrases):
        try:
            led_off()
        except Exception as e:
            print("led_off error:", e)
        speak("All LEDs turned off.")
        return

    # Common quick commands
    if "your name" in task:
        speak("My name is Friday, your personal AI voice assistant.")
        return

    if "who developed you" in task or "who made you" in task:
        speak("I was developed by Dhruv Talwar and his team.")
        return

    if "open youtube" in task:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube.")
        return

    if "time" in task and "what" in task or task == "time":
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {now}.")
        return

    if "date" in task:
        today = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {today}.")
        return

    # fallback: send to Ollama
    response = ollama_chat(task)
    speak(response)

# -----------------------
# General query handler
# -----------------------
def handle_general_query(query: str):
    if not query:
        return
    q_low = query.lower().strip()
    if q_low in EXIT_COMMANDS:
        speak("Going to sleep. Call me anytime, sir.")
        stop_speaking()
        sys.exit(0)

    # Local canned replies
    if any(q in q_low for q in ["your name", "what is your name", "who are you"]):
        speak("My name is Friday, your personal AI voice assistant.")
        return

    if any(q in q_low for q in ["who developed you", "who made you", "who created you"]):
        speak("I was developed by Dhruv Talwar and his team.")
        return

    if "how are you" in q_low:
        speak("I'm functioning perfectly, sir. How can I assist you?")
        return

    # else send to Ollama
    try:
        reply = ollama_chat(query)
        if not reply:
            reply = random.choice(FALLBACK_RESPONSES)
        speak(reply)
    except SystemExit:
        raise
    except Exception as e:
        print("Error in handle_general_query:", e)
        speak("Sorry sir, I couldn't process that right now.")

# -----------------------
# Speech recognition helper
# -----------------------
def takeCommand(timeout: int = 6, phrase_time_limit: int = 6) -> str:
    """
    Listen from the default microphone and return recognized text lower-cased.
    Returns "none" on failure.
    """
    if sr is None:
        print("speech_recognition not available; returning 'none'")
        return "none"

    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("\nListening.....")
            r.pause_threshold = 1
            # optionally adjust for ambient noise:
            try:
                r.adjust_for_ambient_noise(source, duration=0.5)
            except Exception:
                pass
            try:
                audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            except Exception as e:
                print("Microphone listening error:", e)
                return "none"
    except Exception as e:
        print("Microphone open error:", e)
        return "none"

    try:
        print("Understanding...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
        return query.lower()
    except sr.UnknownValueError:
        print("Could not understand audio")
        return "none"
    except sr.RequestError as e:
        print("Speech recognition error:", e)
        return "none"
    except Exception as e:
        print("Recognition exception:", e)
        return "none"

# -----------------------
# Alarm wrapper
# -----------------------
def handle_alarm():
    try:
        set_alarm_with_ring(speak, takeCommand)
    except Exception as e:
        speak("Sorry sir, there was an error setting the alarm.")
        print("Alarm Error:", e)

# -----------------------
# Password check
# -----------------------
def require_password() -> bool:
    pw_file = "password.txt"
    if not os.path.exists(pw_file):
        with open(pw_file, "w") as f:
            f.write("admin")
    for i in range(3):
        try:
            a = input("Enter password to open Friday: ")
        except EOFError:
            return False
        with open(pw_file, 'r') as f:
            pw = f.read().strip()
        if a == pw:
            print("WELCOME SIR! PLEASE SPEAK [WAKE UP] TO LOAD ME UP")
            return True
        elif i == 2:
            return False
        else:
            print("Try again!!")
    return False

# -----------------------
# Main assistant
# -----------------------
def assistant_main():
    try:
        play_gif()
    except Exception:
        pass

    if not require_password():
        print("Authentication failed. Exiting.")
        return

    speak("Hello sir! I am ready. Say wake up to activate me.")
    time.sleep(0.3)

    while True:
        query = takeCommand()
        if not query or query == "none":
            continue
        q_low = query.lower().strip()

        # Split into tasks on specific conjunctions, but keep safety: only split when meaningful
        parts = re.split(r"\b(?:and then|and|also|then|after that)\b", q_low)
        parts = [p.strip() for p in parts if p.strip()]

        if len(parts) > 1:
            speak("Processing multiple commands, sir.")
            # Execute sequentially, but avoid race conditions on hardware by small pauses
            for idx, task in enumerate(parts):
                # show the subtask
                speak(f"Executing: {task}")
                handle_single_task(task)
                # tiny pause between hardware tasks to allow hardware to settle
                time.sleep(0.25)
            continue

        if q_low in EXIT_COMMANDS:
            speak("Ok sir, you can call me anytime.")
            stop_speaking()
            sys.exit(0)

        if "wake up" in q_low:
            print("=====Friday Activated=====\n")
            try:
                greetMe()
            except Exception:
                pass

            # ACTIVATED LOOP
            while True:
                query = takeCommand()
                if not query or query == "none":
                    continue
                q_low = query.lower().strip()

                if q_low in EXIT_COMMANDS:
                    speak("Ok sir, you can call me anytime.")
                    stop_speaking()
                    sys.exit(0)

                try:
                    # Local system commands first (non-Ollama)
                    if "focus mode" in q_low:
                        choice_val = input("Enter focus mode [1=Yes / 2=No]: ")
                        try:
                            if int(choice_val) == 1:
                                speak("Entering the focus mode....")
                                script_path = r"C:\Users\ASUS\OneDrive\Attachments\Desktop\Fri-Day\FocusMode.py"
                                try:
                                    subprocess.run(["powershell", "-Command", f'Start-Process python \"{script_path}\" -Verb runAs'])
                                except Exception as e:
                                    speak("Failed to start focus mode.")
                                    print("Focus mode error:", e)
                            else:
                                speak("Cancelled focus mode.")
                        except ValueError:
                            speak("Invalid selection.")

                    elif "show my focus graph" in q_low:
                        try:
                            focus_graph()
                        except Exception:
                            speak("Focus graph not available.")

                    elif "next tab" in q_low:
                        speak("Switching to next tab, sir.")
                        switch_tab("next")

                    elif "previous tab" in q_low or "back tab" in q_low:
                        speak("Switching to previous tab, sir.")
                        switch_tab("previous")

                    elif "switch window" in q_low or "next window" in q_low:
                        speak("Switching to next window, sir.")
                        switch_app()

                    elif "switch to" in q_low and "switch to tab" not in q_low:
                        app_name = q_low.replace("switch to", "").strip()
                        focus_app(app_name)

                    elif "open new tab" in q_low or "new tab" in q_low:
                        open_new_tab()

                    elif "go to tab" in q_low or "switch to tab" in q_low:
                        nums = [int(w) for w in q_low.split() if w.isdigit()]
                        if nums:
                            switch_to_tab_number(nums[0])
                        else:
                            speak("Please say a tab number between one and nine.")

                    elif "close this tab" in q_low or "close tab" in q_low:
                        close_tab()

                    elif "reopen closed tab" in q_low or "restore tab" in q_low:
                        reopen_closed_tab()

                    elif "show desktop" in q_low or "go to desktop" in q_low:
                        show_desktop()

                    elif "minimize" in q_low:
                        minimize_window()

                    elif "maximize" in q_low:
                        maximize_window()

                    elif "translate" in q_low:
                        translategl(q_low.replace("friday", "").replace("translate", "").strip())

                    elif q_low.startswith("open "):
                        target = q_low.replace("open", "").replace("friday", "").strip()
                        if pag:
                            pag.press("winleft")
                            pag.typewrite(target)
                            time.sleep(0.8)
                            pag.press("enter")
                        else:
                            speak("pyautogui not available to open the application.")

                    elif q_low.startswith("close "):
                        speak(f"Closing {q_low.replace('close', '').strip()} sir.")
                        if pag:
                            pag.hotkey("alt", "f4")
                        else:
                            speak("pyautogui not available to close the application.")

                    elif "google " in q_low:
                        searchGoogle(query)

                    elif "youtube " in q_low:
                        searchYouTube(query)

                    elif "wikipedia " in q_low:
                        searchWikipedia(query)

                    elif "play a game" in q_low:
                        game_play()

                    elif "set an alarm" in q_low:
                        handle_alarm()

                    elif "stop the alarm" in q_low:
                        try:
                            stop_alarm()
                            speak("Alarm stopped, sir.")
                        except Exception:
                            speak("Unable to stop alarm, sir.")

                    elif "temperature" in q_low or "weather" in q_low:
                        try:
                            get_weather_data(query, speak)
                        except Exception:
                            speak("Weather module error.")

                    elif q_low == "pause":
                        if pag:
                            pag.press("k")
                        speak("Video paused, sir!")

                    elif q_low == "play":
                        if pag:
                            pag.press("k")
                        speak("Video played, sir!")

                    elif q_low == "mute":
                        if pag:
                            pag.press("m")
                        speak("Video muted, sir!")

                    elif q_low == "unmute":
                        if pag:
                            pag.press("m")
                        speak("Video unmuted, sir!")

                    elif "volume up" in q_low:
                        speak("Turning volume up, sir!")
                        volumeup()

                    elif "volume down" in q_low:
                        speak("Turning volume down, sir!")
                        volumedown()

                    elif "remember that" in q_low:
                        rememberMessage = q_low.replace("remember that", "").replace("friday", "").strip()
                        speak("You told me that " + rememberMessage)
                        with open("remember.txt", "a") as f:
                            f.write(rememberMessage + "\n")

                    elif "what do you remember" in q_low:
                        try:
                            with open("remember.txt", "r") as f:
                                data = f.read().strip()
                                if data:
                                    speak("You told me to remember: " + data)
                                else:
                                    speak("I don't have any memories, sir.")
                        except FileNotFoundError:
                            speak("No memories found, sir.")

                    elif "tired" in q_low:
                        speak("Playing your favourite songs, sir!")
                        songs = [
                            "https://www.youtube.com/watch?v=K9R7KcaettM",
                            "https://www.youtube.com/watch?v=-YlmnPh-6rE",
                            "https://www.youtube.com/watch?v=5GCfYLguTIs",
                            "https://www.youtube.com/watch?v=Z8IRRphKFZA"
                        ]
                        webbrowser.open(random.choice(songs))

                    elif "news" in q_low:
                        latestNews(speak)

                    elif "calculate" in q_low:
                        try:
                            from calulator import Calc
                            Calc(q_low.replace("calculate", "").strip())
                        except Exception:
                            speak("Calculator module not available.")

                    elif "send whatsapp message" in q_low:
                        sendMessage()

                    elif "shutdown system" in q_low:
                        speak("Are you sure sir?")
                        shutdown = input("Do you wish to shutdown the system? (yes/no): ")
                        if shutdown.lower() == "yes":
                            os.system("shutdown /s /t 1")
                        else:
                            speak("Cancelled shutdown.")

                    elif "change password" in q_low:
                        speak("What's the new password?")
                        new_pw = input("Enter the new password: ")
                        with open("password.txt", 'w') as new_password:
                            new_password.write(new_pw)
                        speak("Done sir!")
                        speak(f"Your new password is: {new_pw}")

                    elif "schedule my day" in q_low:
                        speak("Do you want to clear old tasks, sir? Please say yes or no.")
                        confirm = takeCommand().lower()
                        if "yes" in confirm:
                            open("tasks.txt", "w").close()
                            speak("Old tasks cleared successfully, sir.")
                        else:
                            speak("Keeping old tasks, sir.")
                        try:
                            no_tasks = int(input("Enter the number of tasks: "))
                        except ValueError:
                            speak("Invalid input, sir.")
                            no_tasks = 0
                        for i in range(no_tasks):
                            task = input(f"Enter task {i + 1}: ")
                            with open("tasks.txt", "a") as f:
                                f.write(f"{i + 1}. {task}\n")
                        if no_tasks > 0:
                            speak(f"Your {no_tasks} tasks have been added successfully, sir.")

                    elif "internet speed" in q_low:
                        speak("Checking internet speed, sir.")
                        download, upload = getSpeed()
                        speak(f"Your download speed is {download:.2f} megabits per second")
                        speak(f"Your upload speed is {upload:.2f} megabits per second")

                    elif "score" in q_low or "cricket" in q_low:
                        speak("Fetching cricket updates, sir. Please wait.")
                        live_cricket_score_interactive()

                    elif "screenshot" in q_low:
                        speak("Taking screenshot, sir.")
                        try:
                            path = take_screenshot()
                        except Exception:
                            path = "screenshot_path_placeholder"
                        speak(f"Screenshot saved successfully at {path}")

                    elif "click my photo" in q_low:
                        speak("Taking your photo, sir.")
                        if pag:
                            pag.press("winleft")
                            pag.typewrite("camera")
                            pag.press("enter")
                            time.sleep(2)
                            speak("Say cheese in 3 seconds!")
                            pag.press("enter")
                        else:
                            speak("Camera automation not available.")

                    elif "start typing" in q_low or "voice typing" in q_low:
                        voice_typing_mode()

                    elif "recommend me" in q_low:
                        speak("Entering Suggest Mode, sir.")
                        try:
                            from assistant import run_suggest_mode
                            run_suggest_mode()
                        except Exception as e:
                            speak("Sorry sir, something went wrong in Suggest Mode.")
                            print("Suggest Mode error:", e)

                    elif "brightness" in q_low:
                        brightness_control()

                    elif "explain this code" in q_low or "explain code" in q_low:
                        speak("Sure sir, please paste the code you want me to explain.")
                        print("Paste your code below. Type 'END' on a new line to finish:")
                        user_code_lines = []
                        while True:
                            line = input()
                            if line.strip().upper() == "END":
                                break
                            user_code_lines.append(line)
                        user_code = "\n".join(user_code_lines)
                        if not user_code.strip():
                            speak("No code was provided, sir. Returning to normal mode.")
                            continue
                        speak("Which programming language is this code in, sir?")
                        lang = input("Enter language (e.g., Python, C++, Java): ").strip() or "Python"
                        explain_code_via_gemini(user_code, language=lang)

                    elif "pick the call" in q_low:
                        pick_call()

                    elif "reject the call" in q_low:
                        reject_call()

                    elif any(k in q_low for k in ["summarize document", "summarise document", "summarize pdf", "summarise pdf"]):
                        speak("Please provide the file path, sir.")
                        file_path = input("Enter PDF or Word file path: ")
                        if file_path.endswith(".pdf"):
                            text = read_pdf(file_path)
                        elif file_path.endswith(".docx"):
                            text = read_docx(file_path)
                        else:
                            speak("Unsupported file format, sir!")
                            continue
                        speak("Summarizing the document, sir. Please wait...")
                        summary = summarize_text(text)
                        print("\n--- Summary ---\n", summary)

                    elif "turn on led a" in q_low or "led 3 on" in q_low:
                        led_on(3)
                        speak("LED A turned on.")
                        continue

                    elif "turn on led b" in q_low or "led 5 on" in q_low:
                        led_on(5)
                        speak("LED B turned on.")
                        continue

                    elif "turn on led c" in q_low or "led 7 on" in q_low:
                        led_on(7)
                        speak("LED C turned on.")
                        continue

                    elif any(p in q_low for p in ["turn off leds", "turn off all leds", "all leds off", "turn off lights"]):
                        led_off()
                        speak("All LEDs turned off.")
                        continue

                    else:
                        # Nothing matched locally → send to Ollama
                        handle_general_query(query)

                except SystemExit:
                    raise
                except Exception as e:
                    print("Activated loop error:", e)
                    speak("Sorry sir, I encountered an error while processing that command.")

        elif q_low in EXIT_COMMANDS:
            speak("Ok sir, you can call me anytime.")
            stop_speaking()
            sys.exit(0)

# -----------------------
# Entry point
# -----------------------
if __name__ == "__main__":
    try:
        assistant_main()
    except KeyboardInterrupt:
        stop_speaking()
        print("\nExiting. Goodbye.")
        sys.exit(0)