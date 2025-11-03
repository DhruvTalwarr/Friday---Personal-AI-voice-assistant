# SwitchTab.py
import pyautogui
import pygetwindow as gw
import time
from speaker import speak

# -------------------- TAB CONTROLS -------------------- #
def switch_tab(direction="next"):
    """Switch between tabs in any browser."""
    if direction == "next":
        pyautogui.hotkey("ctrl", "tab")
    elif direction == "previous":
        pyautogui.hotkey("ctrl", "shift", "tab")
    time.sleep(0.2)

def switch_to_tab_number(num):
    """Switch directly to a tab number (1–9)."""
    if 1 <= num <= 9:
        pyautogui.hotkey("ctrl", str(num))
        speak(f"Moved to tab {num}, sir.")
    else:
        speak("Please say a number between one and nine.")

def open_new_tab():
    pyautogui.hotkey("ctrl", "t")
    speak("Opened a new tab, sir.")

def close_tab():
    pyautogui.hotkey("ctrl", "w")
    speak("Closed the current tab, sir.")

def reopen_closed_tab():
    pyautogui.hotkey("ctrl", "shift", "t")
    speak("Reopened last closed tab, sir.")

# -------------------- WINDOW CONTROLS -------------------- #
def switch_app():
    """Switch between open windows."""
    pyautogui.hotkey("alt", "tab")

def focus_app(app_name):
    """Focus a specific window by title."""
    windows = gw.getWindowsWithTitle(app_name)
    if windows:
        windows[0].activate()
        speak(f"Switched to {app_name}, sir.")
    else:
        speak(f"Sorry sir, I couldn’t find {app_name} window.")

def show_desktop():
    pyautogui.hotkey("win", "d")
    speak("Showing desktop, sir.")

def minimize_window():
    """Minimize current window."""
    active = gw.getActiveWindow()
    if active:
        active.minimize()
        speak("Window minimized, sir.")
    else:
        speak("No active window found, sir.")

def maximize_window():
    """Maximize current window."""
    active = gw.getActiveWindow()
    if active:
        active.maximize()
        speak("Window maximized, sir.")
    else:
        speak("No active window found, sir.")

def restore_window():
    """Restore a minimized window."""
    active = gw.getActiveWindow()
    if active:
        active.restore()
        speak("Window restored, sir.")
    else:
        speak("No active window to restore, sir.")
