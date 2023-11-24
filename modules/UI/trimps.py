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
        self.upgrade_region = (15,695,1060,690)
        self.warpstation_screenshot = "warpstation"

    def try_play_trimps(self):
        # update play button
        self.is_playing_trimps = not self.is_playing_trimps
        button_text = "stop" if self.is_playing_trimps else "play" 
        background = "red" if self.is_playing_trimps else "green"
        self.application.trimps_button.config(text=button_text, background=background)
        
        if self.is_playing_trimps:
            self.application.master.after(10, self.play_trimps_loop)

    def play_trimps_loop(self):
        warpstation_button_location = self.get_button_location(self.warpstation_screenshot, self.warpstation_screenshot)

        if warpstation_button_location != None:
            pyautogui.moveTo(warpstation_button_location.x, warpstation_button_location.y)
            pyautogui.click()


    def get_button_location(self, button_screenshot_name, region: tuple[int,int,int,int] | None) -> pyautogui.Point | None:
        button_location = None
        try:
            # the region param is (left, top, width, height)
            button_location = pyautogui.locateCenterOnScreen(f'screenshots/{button_screenshot_name}.png', region=region, confidence=0.7)
        except:
            print(f"{button_screenshot_name} not found")
        else:
            print(f'found {button_screenshot_name} at {button_location}')
            return button_location
        
        return None