import threading
import time
import re
import datetime
import os
import pygame

# --- Configuration ---
ALARM_SOUND_FILE = os.path.join(os.getcwd(), "soft_morning_alarm.mp3")
# ---------------------

# Global variable to control alarm
alarm_playing = False

def stop_alarm():
    """Stops the currently playing alarm."""
    global alarm_playing
    if alarm_playing:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        alarm_playing = False
        print("Alarm stopped.")
    else:
        print("No alarm is currently playing.")

def set_alarm_with_ring(speak_func, takeCommand_func):
    """Sets a non-blocking alarm that can be stopped."""
    global alarm_playing

    speak_func("At what time should I set the alarm, sir?")
    time_query = takeCommand_func()

    if time_query.lower() == "none":
        speak_func("I didn't catch the time. Please try again.")
        return

    match = re.search(r'(\d{1,2})(?::(\d{1,2}))?\s*(a\.?m\.?|p\.?m\.?)', time_query, re.IGNORECASE)
    if not match:
        speak_func("I couldn't understand the time format. Please say it clearly with AM or PM.")
        return

    hour = int(match.group(1))
    minute = int(match.group(2)) if match.group(2) else 0
    meridiem = match.group(3).lower().replace('.', '')

    if meridiem == 'pm' and hour != 12:
        hour += 12
    elif meridiem == 'am' and hour == 12:
        hour = 0

    now = datetime.datetime.now()
    target_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
    if target_time <= now:
        target_time += datetime.timedelta(days=1)

    time_diff = (target_time - now).total_seconds()

    def alarm_thread_target():
        global alarm_playing
        time.sleep(time_diff)
        speak_func("Sir, the alarm time has been reached.")

        if not os.path.exists(ALARM_SOUND_FILE):
            speak_func("Alarm sound file not found. Please check the file path.")
            return

        try:
            pygame.mixer.init()
            pygame.mixer.music.load(ALARM_SOUND_FILE)
            pygame.mixer.music.play(-1)  # -1 loops indefinitely until stopped
            alarm_playing = True

            # Keep thread alive while alarm is playing
            while alarm_playing and pygame.mixer.music.get_busy():
                time.sleep(1)

            pygame.mixer.music.stop()
            pygame.mixer.quit()
            alarm_playing = False

        except Exception as e:
            speak_func("I attempted to play the alarm sound, but an error occurred.")
            print(f"Alarm Sound Error: {e}")

    threading.Thread(target=alarm_thread_target, daemon=True).start()
    speak_func(f"Alarm successfully set for {target_time.strftime('%I:%M %p')}. I will ring the alarm.")

