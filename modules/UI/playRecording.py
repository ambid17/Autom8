from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
import time
import json
import sys
import tkinter as tk
import os
from tkinter import ttk

class PlayRecording:
    def __init__(self, application):
        self.application = application

        self.application.play_label = tk.Label(self.application.buttonBar, text="File Name:")
        self.application.play_label.grid(row = 2, column=0, pady = 2)

        self.play_var = tk.StringVar()
        self.application.play_combo_box = ttk.Combobox(self.application.buttonBar, textvariable=self.play_var)
        self.application.play_combo_box.grid(row = 2, column=1, pady = 2)
        self.application.play_combo_box['values'] = os.listdir("recordedCommands") 

        self.application.play_button = tk.Button(self.application.buttonBar, width=15, height=5, command=self.playRecording, background="red", text="play macro")
        self.application.play_button.grid(row = 2, column=2, pady = 2)

    def getRecordings(self):
        files = os.listdir("recordedCommands") 
    

    def playRecording(self):
        file_path = "recordedCommands/" + self.play_var.get()
        with open(file_path) as json_file:
            data = json.load(json_file)

        special_keys = {
            "Key.shift": Key.shift, 
            "Key.tab": Key.tab, 
            "Key.caps_lock": Key.caps_lock, 
            "Key.ctrl": Key.ctrl, 
            "Key.alt": Key.alt, 
            "Key.cmd": Key.cmd, 
            "Key.cmd_r": Key.cmd_r, 
            "Key.alt_r": Key.alt_r, 
            "Key.ctrl_r": Key.ctrl_r, 
            "Key.shift_r": Key.shift_r, 
            "Key.enter": Key.enter, 
            "Key.backspace": Key.backspace, 
            "Key.f19": Key.f19, 
            "Key.f18": Key.f18, 
            "Key.f17": Key.f17, 
            "Key.f16": Key.f16, 
            "Key.f15": Key.f15, 
            "Key.f14": Key.f14, 
            "Key.f13": Key.f13, 
            "Key.media_volume_up": Key.media_volume_up, 
            "Key.media_volume_down": Key.media_volume_down, 
            "Key.media_volume_mute": Key.media_volume_mute, 
            "Key.media_play_pause": Key.media_play_pause, 
            "Key.f6": Key.f6, 
            "Key.f5": Key.f5, 
            "Key.right": Key.right, 
            "Key.down": Key.down, 
            "Key.left": Key.left, 
            "Key.up": Key.up, 
            "Key.page_up": Key.page_up, 
            "Key.page_down": Key.page_down, 
            "Key.home": Key.home, 
            "Key.end": Key.end, 
            "Key.delete": Key.delete, 
            "Key.space": Key.space,
            "Key.esc": Key.esc
            }

        mouse = MouseController()
        keyboard = KeyboardController()

        for index, obj in enumerate(data):
            action, _time= obj['action'], obj['_time']
            try:
                next_movement = data[index+1]['_time']
                pause_time = next_movement - _time
            except IndexError as e:
                pause_time = 1
            
            if action == "pressed_key" or action == "released_key":
                key = obj['key'] if 'Key.' not in obj['key'] else special_keys[obj['key']]
                print("action: {0}, time: {1}, key: {2}".format(action, _time, str(key)))
                if action == "pressed_key":
                    keyboard.press(key)
                else:
                    keyboard.release(key)
                time.sleep(pause_time)


            else:
                move_for_scroll = True
                x, y = obj['x'], obj['y']
                if action == "scroll" and index > 0 and (data[index - 1]['action'] == "pressed" or data[index - 1]['action'] == "released"):
                    if x == data[index - 1]['x'] and y == data[index - 1]['y']:
                        move_for_scroll = False
                print("x: {0}, y: {1}, action: {2}, time: {3}".format(x, y, action, _time))
                mouse.position = (x, y)
                if action == "pressed" or action == "released" or action == "scroll" and move_for_scroll == True:
                    time.sleep(0.1)
                if action == "pressed":
                    mouse.press(Button.left if obj['button'] == "Button.left" else Button.right)
                elif action == "released":
                    mouse.release(Button.left if obj['button'] == "Button.left" else Button.right)
                elif action == "scroll":
                    horizontal_direction, vertical_direction = obj['horizontal_direction'], obj['vertical_direction']
                    mouse.scroll(horizontal_direction, vertical_direction)
                time.sleep(pause_time)
    

