import sys
import tkinter as tk
from pynput import mouse
from pynput import keyboard

class Trimps:
    def __init__(self, application):
        self.application = application

        self.application.trimps_label = tk.Label(self.application.buttonBar, text="Play trimps")
        self.application.trimps_label.grid(row = 3, column=0, pady = 2)

        self.application.trimps_button = tk.Button(self.application.buttonBar, width=15, height=5, command=self.play_trimps, background="green", text="play")
        self.application.trimps_button.grid(row = 3, column=1, pady = 2)
        

        self.is_playing_trimps = False

    def play_trimps(self):
        print("test")
        self.is_playing_trimps = not self.is_playing_trimps
        button_text = "stop" if self.is_playing_trimps else "play" 
        background = "red" if self.is_playing_trimps else "green"
        self.application.trimps_button.config(text=button_text, background=background)
        #self.application.trimps_button