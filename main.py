import pyautogui
import keyboard
import time
import numpy as np
import random
# 7import win32api, win32con

from modules import unity
from modules import utils



commands = ["1. command = track : track mouse position", "2. command = unity : open unity workspace", "3. command = record : record input"]
commandRequest = "what do ya wanna do?: \n"

for command in commands:
    commandRequest += command + "\n"

command = input(commandRequest)

if command == "1" or command == "track":
    utils.trackMousePos()
if command == "2" or command == "unity":
    unity.openUnityWorkspace()
if command == "3" or command == "record":
    utils.recordInput()



