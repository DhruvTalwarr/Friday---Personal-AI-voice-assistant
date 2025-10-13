import threading
import time
import re
import datetime
import speech_recognition as sr
import playsound # NEW IMPORT

# --- Configuration ---
# You must place this file in the same directory as this script!
ALARM_SOUND_FILE = "soft_morning_alarm.mp3"
# ---------------------

def set_alarm_with_ring(speak_func, takeCommand_func):
    """Prompts user for a time and sets a non-blocking thread to play an MP3 alarm."""
    
    speak_func("At what time should I set the alarm, sir?")
    
    # 1. Listen for the user's specific time command
    time_query = takeCommand_func() 
    
    if time_query.lower() == "none":
        speak_func("I didn't catch the time. Please try setting the alarm again.")
        return

    # --- Time Parsing Logic ---
    match = re.search(r'(\d+)\s*(\d*)\s*(a\.?m\.?|p\.?m\.?)', time_query, re.IGNORECASE)
    
    if match:
        hour = int(match.group(1))
        minute_str = match.group(2)
        meridiem = match.group(3).lower()
        
        minute = int(minute_str) if minute_str else 0

        # Convert 12-hour time to 24-hour time
        if meridiem in ('p.m.', 'pm') and hour != 12:
            hour += 12
        elif meridiem in ('a.m.', 'am') and hour == 12:
            hour = 0

        # Calculate Wait Time
        now = datetime.datetime.now()
        target_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
        
        if target_time <= now:
            target_time += datetime.timedelta(days=1)
        
        time_diff = (target_time - now).total_seconds()
        
        # --- Set the Non-Blocking Alarm Thread ---
        
        def alarm_thread_target():
            # Wait for the calculated duration
            time.sleep(time_diff)
            
            # 🔊 Play the MP3 alarm sound
            try:
                # Speak first to alert the user, then play the sound
                speak_func("Sir, the alarm time has been reached.")
                playsound(ALARM_SOUND_FILE)
            except Exception as e:
                speak_func("I attempted to play the alarm sound, but an error occurred.")
                print(f"Alarm Sound Error: {e}")

        # Start the thread
        alarm_thread = threading.Thread(target=alarm_thread_target)
        alarm_thread.start()
        
        # Provide confirmation to the user immediately
        speak_func(f"Alarm successfully set for {target_time.strftime('%I:%M %p')}. I will ring the alarm.")

    else:
        speak_func("I couldn't understand the time format. Please try again with a clear time and AM or PM.")