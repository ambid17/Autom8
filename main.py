import pyautogui
import keyboard
import time
import numpy as np
import random
import os
import tkinter as tk
import datetime
# 7import win32api, win32con

from modules import unity
from modules import utils
from modules import record
from modules import playRecording
from modules import screenshot




# commands = ["1. command = track : track mouse position", 
#             "2. command = unity : open unity workspace", 
#             "3. command = record : record input",
#             "4. command = play : play a recording",
#             "5. command = screen : take a screenshot"
#             ]


# commandRequest = "Commands:\n"
# for command in commands:
#     commandRequest += command + "\n"
# commandRequest += "what do ya wanna do?:  "
# command = input(commandRequest)

# if command == "1" or command == "track":
#     utils.trackMousePos()
# if command == "2" or command == "unity":
#     unity.openUnityWorkspace()
# if command == "3" or command == "record":
#     file_name = input("choose a file name:\n")
#     record.start_recording(file_name, False)
# if command == "4" or command == "play":
#     files = os.listdir("recordedCommands")

#     file_name_string = "Recordings:\n"

#     index = 0
#     for file in files:
#         file_name_string += f'{index}. {file}\n'
#         index += 1

#     file_name_string += "choose a file to play (type index or full file name):   "
#     file_name = input(file_name_string)

#     file_selected_index = int(file_name)

#     file_name = files[file_selected_index]
#     playRecording.playRecording(file_name)
# if command == "5" or command == "screen":
#     screenshot.takeScreenshot()


class Application:
    def __init__(self, master):
        self.snip_surface = None
        self.master = master
        self.start_x = None
        self.start_y = None
        self.current_x = None
        self.current_y = None

        root.geometry('400x50+200+200')  # set new geometry
        root.title('Autom8')

        self.menu_frame = tk.Frame(master)
        self.menu_frame.pack(fill=tk.BOTH, expand=tk.YES, padx=1, pady=1)

        self.buttonBar = tk.Frame(self.menu_frame, bg="")
        self.buttonBar.pack()

        self.snipButton = tk.Button(self.buttonBar, width=15, height=5, command=self.create_screen_canvas, background="green", text="screenshot")
        self.snipButton.pack()

        self.master_screen = tk.Toplevel(root)
        self.master_screen.withdraw()
        self.master_screen.attributes("-transparent", "maroon3")
        self.picture_frame = tk.Frame(self.master_screen, background="maroon3")
        self.picture_frame.pack(fill=tk.BOTH, expand=tk.YES)

    def create_screen_canvas(self):
        self.master_screen.deiconify()
        root.withdraw()

        self.snip_surface = tk.Canvas(self.picture_frame, cursor="cross", bg="grey11")
        self.snip_surface.pack(fill=tk.BOTH, expand=tk.YES)

        self.snip_surface.bind("<ButtonPress-1>", self.on_button_press)
        self.snip_surface.bind("<B1-Motion>", self.on_snip_drag)
        self.snip_surface.bind("<ButtonRelease-1>", self.on_button_release)

        self.master_screen.attributes('-fullscreen', True)
        self.master_screen.attributes('-alpha', .3)
        self.master_screen.lift()
        self.master_screen.attributes("-topmost", True)

    def on_button_release(self, event):
        self.display_rectangle_position()

        if self.start_x <= self.current_x and self.start_y <= self.current_y:
            print("right down")
            utils.take_bounded_screenshot(self.start_x, self.start_y, self.current_x - self.start_x, self.current_y - self.start_y)

        elif self.start_x >= self.current_x and self.start_y <= self.current_y:
            print("left down")
            utils.take_bounded_screenshot(self.current_x, self.start_y, self.start_x - self.current_x, self.current_y - self.start_y)

        elif self.start_x <= self.current_x and self.start_y >= self.current_y:
            print("right up")
            utils.take_bounded_screenshot(self.start_x, self.current_y, self.current_x - self.start_x, self.start_y - self.current_y)

        elif self.start_x >= self.current_x and self.start_y >= self.current_y:
            print("left up")
            utils.take_bounded_screenshot(self.current_x, self.current_y, self.start_x - self.current_x, self.start_y - self.current_y)

        self.exit_screenshot_mode()
        return event

    def exit_screenshot_mode(self):
        self.snip_surface.destroy()
        self.master_screen.withdraw()
        root.deiconify()

    def on_button_press(self, event):
        # save mouse drag start position
        self.start_x = self.snip_surface.canvasx(event.x)
        self.start_y = self.snip_surface.canvasy(event.y)
        self.snip_surface.create_rectangle(0, 0, 1, 1, outline='red', width=3, fill="maroon3")

    def on_snip_drag(self, event):
        self.current_x, self.current_y = (event.x, event.y)
        # expand rectangle as you drag the mouse
        self.snip_surface.coords(1, self.start_x, self.start_y, self.current_x, self.current_y)

    def display_rectangle_position(self):
        print(self.start_x)
        print(self.start_y)
        print(self.current_x)
        print(self.current_y)


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()

