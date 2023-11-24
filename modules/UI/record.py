from pynput import mouse
from pynput import keyboard
import time
import json
import sys
import tkinter as tk
from main import Application

# yoinked pynput code from: https://github.com/george-jensen/record-and-play-pynput/blob/main/record.py
class Record:
    def __init__(self, application: Application):
        self.application = application
        self.application.record_label = tk.Label(self.application.buttonBar, text="File Name:")
        self.application.record_label.grid(row = 1, column=0, pady = 2)

        self.record_var = tk.StringVar()
        self.record_var.trace('w', self.set_file_name)
        self.application.record_entry = tk.Entry(self.application.buttonBar, textvariable=self.record_var)
        self.application.record_entry.grid(row = 1, column=1, pady = 2)

        self.application.record_button = tk.Button(self.application.buttonBar, width=15, height=5, command=self.start_recording, background="red", text="record macro")
        self.application.record_button.grid(row = 1, column=2, pady = 2)

        self.record_all = False

        self.storage = []
        self.count = 0
        self.keyboard_listener = []
        self.mouse_listener = []

    def set_file_name(self, *args):
        self.file_name = self.record_var.get()

    def try_quit(self):
        if len(self.storage) > 1:
            print(f'last: {self.storage[-1]}')
            is_released = self.storage[-1]['action'] == 'released_key'
            is_esc = self.storage[-1]['key'] == 'Key.esc'
            print(f'last: {self.storage[-1]} released: {is_released} esc: {is_esc}')
            if self.storage[-1]['action'] == 'released_key' and self.storage[-1]['key'] == 'Key.esc':
                print("testing")
                print(f'file name": {self.file_name}')
                file_path = f'recordedCommands/{self.file_name}.txt'
                print(f'saving recording to {file_path}')
                with open(file_path, 'w') as outfile:
                    json.dump(self.storage, outfile)
                self.mouse_listener.stop()
                self.keyboard_listener.stop()
                return False
        return True

    def on_press(self, key):
        should_continue = self.try_quit()

        if should_continue == False:
            return False
        try:
            json_object = {'action':'pressed_key', 'key':key.char, '_time': time.time()}
        except AttributeError:
            json_object = {'action':'pressed_key', 'key':str(key), '_time': time.time()}
        self.storage.append(json_object)

    def on_release(self, key):
        try:
            json_object = {'action':'released_key', 'key':key.char, '_time': time.time()}
        except AttributeError:
            json_object = {'action':'released_key', 'key':str(key), '_time': time.time()}
        self.storage.append(json_object)
            

    def on_move(self, x, y):
        if (self.record_all) == True:
            if len(self.storage) >= 1:
                if self.storage[-1]['action'] != "moved":
                    json_object = {'action':'moved', 'x':x, 'y':y, '_time':time.time()}
                    self.storage.append(json_object)
                elif self.storage[-1]['action'] == "moved" and time.time() - self.storage[-1]['_time'] > 0.02:
                    json_object = {'action':'moved', 'x':x, 'y':y, '_time':time.time()}
                    self.storage.append(json_object)
            else:
                json_object = {'action':'moved', 'x':x, 'y':y, '_time':time.time()}
                self.storage.append(json_object)
        else:
            if len(self.storage) >= 1:
                if (self.storage[-1]['action'] == "pressed" and self.storage[-1]['button'] == 'Button.left') or (self.storage[-1]['action'] == "moved" and time.time() - self.storage[-1]['_time'] > 0.02):
                    json_object = {'action':'moved', 'x':x, 'y':y, '_time':time.time()}
                    self.storage.append(json_object)

    def on_click(self, x, y, button, pressed):
        json_object = {'action':'pressed' if pressed else 'released', 'button':str(button), 'x':x, 'y':y, '_time':time.time()}
        self.storage.append(json_object)
        


    def on_scroll(self, x, y, dx, dy):
        json_object = {'action': 'scroll', 'vertical_direction': int(dy), 'horizontal_direction': int(dx), 'x':x, 'y':y, '_time': time.time()}
        self.storage.append(json_object)


    def start_recording(self):
        print("Hit 'escape' to finish recording")

        self.keyboard_listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        )

        self.mouse_listener = mouse.Listener(
            on_click=self.on_click,
            on_scroll=self.on_scroll,
            on_move=self.on_move
        )

        self.keyboard_listener.start()
        self.mouse_listener.start()
        self.keyboard_listener.join()
        self.mouse_listener.join()