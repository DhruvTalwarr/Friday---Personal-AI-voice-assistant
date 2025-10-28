# speak.py
import pyttsx3
import threading
import queue

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.setProperty('rate', 170)

_speak_queue = queue.Queue()

def _process_queue():
    while True:
        text = _speak_queue.get()
        if text is None:
            break
        engine.say(text)
        engine.runAndWait()
        _speak_queue.task_done()

_thread = threading.Thread(target=_process_queue, daemon=True)
_thread.start()

def speak(text):
    print(f"Friday: {text}")
    _speak_queue.put(text)

def stop_speaking():
    engine.stop()
    with _speak_queue.mutex:
        _speak_queue.queue.clear()
