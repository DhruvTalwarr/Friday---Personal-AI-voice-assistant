# # from tkinter import *
# # from PIL import Image, ImageTk, ImageSequence
# # import time
# # import pygame
# # from pygame import mixer

# # mixer.init()

# # root = Tk()
# # root.geometry("1000x500")


# # def play_gif():
# #     root.lift()
# #     root.attributes("-topmost", True)
# #     global img
# #     img = Image.open("214285.gif")
# #     lbl = Label(root)
# #     lbl.place(x=0, y=0)
# #     i = 0
# #     mixer.music.load("doctor-strange-magic-circle-shield-sound-effect-38335.mp3")
# #     mixer.music.play()
# #     for img in ImageSequence.Iterator(img):
# #         img = img.resize((1000, 500))
# #         img = ImageTk.PhotoImage(img)
# #         lbl.config(image=img)
# #         root.update()
# #         time.sleep(0.01)
# #     root.destroy()

# # play_gif()
# # root.mainloop()

# # Intro.py
# from tkinter import *
# from PIL import Image, ImageTk, ImageSequence
# import time
# import pygame
# from pygame import mixer

# mixer.init()

# def play_gif():
#     # Create a new window (independent)
#     intro_root = Tk()
#     intro_root.geometry("1000x500")
#     intro_root.title("Friday - Initializing")
#     intro_root.configure(bg="black")
#     intro_root.overrideredirect(True)  # Hide title bar
#     intro_root.attributes("-topmost", True)

#     lbl = Label(intro_root, bg="black")
#     lbl.pack(fill="both", expand=True)

#     # Load sound & GIF
#     mixer.music.load("doctor-strange-magic-circle-shield-sound-effect-38335.mp3")
#     mixer.music.play()
#     gif = Image.open("214285.gif")

#     # Play GIF frames
#     try:
#         for frame in ImageSequence.Iterator(gif):
#             frame = frame.resize((1000, 500))
#             frame = ImageTk.PhotoImage(frame)
#             lbl.config(image=frame)
#             intro_root.update_idletasks()
#             intro_root.update()
#             time.sleep(0.01)
#     except TclError:
#         # Window closed early or destroyed
#         pass

#     # Clean up
#     mixer.music.stop()
#     intro_root.destroy()

# Intro.py
from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import time
import pygame
from pygame import mixer

mixer.init()

def play_gif():
    intro_root = Tk()
    intro_root.title("Friday Intro")
    intro_root.configure(bg="black")
    intro_root.overrideredirect(True)  # Hide title bar for cinematic look
    intro_root.attributes("-topmost", True)  # Always on top

    # Get screen dimensions
    screen_width = intro_root.winfo_screenwidth()
    screen_height = intro_root.winfo_screenheight()

    # Desired window size
    window_width = 1000
    window_height = 500

    # Calculate position to center the window
    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    # Apply geometry (position + size)
    intro_root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    lbl = Label(intro_root, bg="black")
    lbl.pack(fill="both", expand=True)

    # Load sound & GIF
    mixer.music.load("doctor-strange-magic-circle-shield-sound-effect-38335.mp3")
    mixer.music.play()
    gif = Image.open("214285.gif")

    try:
        for frame in ImageSequence.Iterator(gif):
            frame = frame.resize((window_width, window_height))
            frame = ImageTk.PhotoImage(frame)
            lbl.config(image=frame)
            intro_root.update_idletasks()
            intro_root.update()
            time.sleep(0.01)
    except TclError:
        # Happens if user closes the window manually
        pass

    # Stop the sound and close after animation
    mixer.music.stop()
    intro_root.destroy()
