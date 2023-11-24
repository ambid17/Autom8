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
from modules.UI import trimps

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
        self.trimps = trimps.Trimps(self)

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

