from pynput.keyboard import Key, Controller
import pyautogui
import time
import os
import datetime
from time import sleep

keyboard = Controller()

def volumeup():
    for i in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)
def volumedown():
    for i in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)



def take_screenshot():
    try:
        # Make a folder to store screenshots
        folder = "Screenshots"
        if not os.path.exists(folder):
            os.mkdir(folder)

        # Filename with timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_path = os.path.join(folder, f"screenshot_{timestamp}.png")

        # Take screenshot
        pyautogui.hotkey('win', 'prtsc')
        time.sleep(1)  # Wait for the OS to save the file

        # Optional manual save for reliability
        pyautogui.screenshot(file_path)

        return file_path

    except Exception as e:
        return str(e)
