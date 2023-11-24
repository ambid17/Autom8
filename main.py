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
from modules.UI import record
from modules.UI import playRecording
from modules.UI import screenshot




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


# yoinked from: https://stackoverflow.com/questions/49901928/how-to-take-a-screenshot-with-python-using-a-click-and-drag-method-like-snipping
class Application:
    def __init__(self, master):
        self.snip_surface = None
        self.master = master
        self.start_x = None
        self.start_y = None
        self.current_x = None
        self.current_y = None
        self.is_tracking_mouse = False

        self.master.geometry('600x800+200+200')  # set new geometry
        self.master.title('Autom8')

        self.menu_frame = tk.Frame(master)
        self.menu_frame.pack(fill=tk.BOTH, expand=tk.YES, padx=1, pady=1)

        self.buttonBar = tk.Frame(self.menu_frame, bg="")
        self.buttonBar.pack()

        self.screenshot = screenshot.Screenshot(self)
        self.record = record.Record(self)
        self.play_recording = playRecording.PlayRecording(self)

        # snipping canvas
        self.master_screen = tk.Toplevel(self.master)
        self.master_screen.withdraw()
        self.master_screen.attributes("-transparent", "maroon3")
        self.picture_frame = tk.Frame(self.master_screen, background="maroon3")
        self.picture_frame.pack(fill=tk.BOTH, expand=tk.YES)

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()

