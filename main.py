import pyautogui
import keyboard
import time
import numpy as np
import random
import os
# 7import win32api, win32con

from modules import unity
from modules import utils
from modules import record
from modules import playRecording



commands = ["1. command = track : track mouse position", 
            "2. command = unity : open unity workspace", 
            "3. command = record : record input",
            "4. command = play : play a recording"
            ]


commandRequest = "Commands:\n"
for command in commands:
    commandRequest += command + "\n"
commandRequest += "what do ya wanna do?:  "
command = input(commandRequest)

if command == "1" or command == "track":
    utils.trackMousePos()
if command == "2" or command == "unity":
    unity.openUnityWorkspace()
if command == "3" or command == "record":
    file_name = input("choose a file name:\n")
    record.start_recording(file_name, False)
if command == "4" or command == "play":
    files = os.listdir("recordedCommands")

    file_name_string = "Recordings:\n"

    index = 0
    for file in files:
        file_name_string += f'{index}. {file}\n'
        index += 1

    file_name_string += "choose a file to play (type index or full file name):   "
    file_name = input(file_name_string)

    file_selected_index = int(file_name)

    file_name = files[file_selected_index]
    playRecording.playRecording(file_name)



