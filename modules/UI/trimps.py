import sys
import tkinter as tk
from pynput import mouse
from pynput import keyboard
from main import Application
import pyautogui


class Trimps:
    def __init__(self, application: Application):
        self.application = application

        self.application.trimps_label = tk.Label(self.application.buttonBar, text="Play trimps")
        self.application.trimps_label.grid(row = 3, column=0, pady = 2)

        self.application.trimps_button = tk.Button(self.application.buttonBar, width=15, height=5, command=self.try_play_trimps, background="green", text="play")
        self.application.trimps_button.grid(row = 3, column=1, pady = 2)
        

        self.is_playing_trimps = False

    def try_play_trimps(self):
        # update play button
        self.is_playing_trimps = not self.is_playing_trimps
        button_text = "stop" if self.is_playing_trimps else "play" 
        background = "red" if self.is_playing_trimps else "green"
        self.application.trimps_button.config(text=button_text, background=background)
        
        if self.is_playing_trimps:
            self.application.master.after(10, self.play_trimps_loop)

    def play_trimps_loop(self):
        warpstation_button_location = None
        try:
            # the region param is (left, top, width, height)
            warpstation_button_location = pyautogui.locateCenterOnScreen('screenshots/test.png', region=(15,695,1060,690), confidence=0.1)
        except:
            print("warpstation not found")

        if warpstation_button_location != None:
            print(warpstation_button_location)
