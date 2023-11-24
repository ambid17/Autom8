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

        self.warpstation_coords: tuple[int,int] = (86, 1003)
        self.warpstation_color: tuple[int,int,int] = (0,37,75)

        self.can_upgrade_color: tuple[int,int,int] = (0,0,0)
        self.gym_coords: tuple[int,int] = (483, 1002)
        self.tribute_coords: tuple[int,int] = (719, 1002)
        self.nursery_coords: tuple[int,int] = (942, 1002)

        # used to make sure the upgrade scroll bar is at the top
        self.upgrade_scroll_bar_coords: tuple[int,int] = (1051, 700)
        self.upgrade_scroll_bar_color: tuple[int,int,int] = (85,85,85)

        self.stop_hotkey = "q"


    def try_play_trimps(self):
        # update play button
        self.is_playing_trimps = not self.is_playing_trimps
        button_text = "stop" if self.is_playing_trimps else "play" 
        background = "red" if self.is_playing_trimps else "green"
        self.application.trimps_button.config(text=button_text, background=background)
        
        if self.is_playing_trimps:
            self.application.root.after(10, self.play_trimps_loop)

            self.keyboard_listener = keyboard.Listener(
                on_press=self.on_press,
            )
            self.keyboard_listener.start()

    def on_press(self, key):
        if(key.char == self.stop_hotkey):
            self.is_playing_trimps = False
            self.keyboard_listener.stop()

            button_text = "stop" if self.is_playing_trimps else "play" 
            background = "red" if self.is_playing_trimps else "green"
            self.application.trimps_button.config(text=button_text, background=background)

    def play_trimps_loop(self):
        upgrade_scrolled_to_top = self.get_button_status(self.upgrade_scroll_bar_coords, self.upgrade_scroll_bar_color)
        if upgrade_scrolled_to_top == False:
            pyautogui.moveTo(self.upgrade_scroll_bar_coords)
            pyautogui.click()

        warpstation_status = self.get_button_status(self.warpstation_coords, self.warpstation_color)
        if warpstation_status == True:
            pyautogui.moveTo(self.warpstation_coords[0], self.warpstation_coords[1])
            pyautogui.click()

        gym_status = self.get_button_status(self.gym_coords, self.can_upgrade_color)
        if gym_status == True:
            pyautogui.moveTo(self.gym_coords[0], self.gym_coords[1])
            pyautogui.click()

        tribute_status = self.get_button_status(self.tribute_coords, self.can_upgrade_color)
        if tribute_status == True:
            pyautogui.moveTo(self.tribute_coords[0], self.tribute_coords[1])
            pyautogui.click()

        nursery_status = self.get_button_status(self.nursery_coords, self.can_upgrade_color)
        if nursery_status == True:
            pyautogui.moveTo(self.nursery_coords[0], self.nursery_coords[1])
            pyautogui.click()

        if self.is_playing_trimps == True:
            self.application.root.after(10, self.play_trimps_loop)


    def get_button_status(self, pixel_coords: tuple[int,int], enabled_color: tuple[int,int,int]):
        return pyautogui.pixelMatchesColor(pixel_coords[0], pixel_coords[1], enabled_color)

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