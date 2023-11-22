import pyautogui
import keyboard
import mouse
import time

def trackMousePos():
    while keyboard.is_pressed('q') == False:
        pos = pyautogui.position()
        print(pos)
        time.sleep(0.5)
