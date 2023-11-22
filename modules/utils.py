import pyautogui
import keyboard
import mouse
import time

def trackMousePos():
    while keyboard.is_pressed('q') == False:
        pos = pyautogui.position()
        print(pos)
        time.sleep(0.5)


def recordInput():
    mouse_events = []
    
    keyboard = keyboard.record(until='esc')
    mouse = mouse.hook(mouse_events.append)
    print(recorded)