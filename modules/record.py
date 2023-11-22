from pynput import mouse
from pynput import keyboard
import time
import json
import sys

name_of_recording = "test"
record_all = False

storage = []
count = 0
keyboard_listener = []
mouse_listener = []

def try_quit():
    if len(storage) > 1:
        if storage[-1]['action'] == 'released_key' and storage[-1]['key'] == 'Key.esc':
            file_path = f'recordedCommands/{name_of_recording}.txt'
            print(f'saving recording to {file_path}')
            with open(file_path, 'w') as outfile:
                json.dump(storage, outfile)
            mouse_listener.stop()
            keyboard_listener.stop()
            return False
    return True

def on_press(key):
    should_continue = try_quit()

    if should_continue == False:
        return False
    try:
        json_object = {'action':'pressed_key', 'key':key.char, '_time': time.time()}
    except AttributeError:
        json_object = {'action':'pressed_key', 'key':str(key), '_time': time.time()}
    storage.append(json_object)

def on_release(key):
    try:
        json_object = {'action':'released_key', 'key':key.char, '_time': time.time()}
    except AttributeError:
        json_object = {'action':'released_key', 'key':str(key), '_time': time.time()}
    storage.append(json_object)
        

def on_move(x, y):
    if (record_all) == True:
        if len(storage) >= 1:
            if storage[-1]['action'] != "moved":
                json_object = {'action':'moved', 'x':x, 'y':y, '_time':time.time()}
                storage.append(json_object)
            elif storage[-1]['action'] == "moved" and time.time() - storage[-1]['_time'] > 0.02:
                json_object = {'action':'moved', 'x':x, 'y':y, '_time':time.time()}
                storage.append(json_object)
        else:
            json_object = {'action':'moved', 'x':x, 'y':y, '_time':time.time()}
            storage.append(json_object)
    else:
        if len(storage) >= 1:
            if (storage[-1]['action'] == "pressed" and storage[-1]['button'] == 'Button.left') or (storage[-1]['action'] == "moved" and time.time() - storage[-1]['_time'] > 0.02):
                json_object = {'action':'moved', 'x':x, 'y':y, '_time':time.time()}
                storage.append(json_object)

def on_click(x, y, button, pressed):
    json_object = {'action':'pressed' if pressed else 'released', 'button':str(button), 'x':x, 'y':y, '_time':time.time()}
    storage.append(json_object)
    


def on_scroll(x, y, dx, dy):
    json_object = {'action': 'scroll', 'vertical_direction': int(dy), 'horizontal_direction': int(dx), 'x':x, 'y':y, '_time': time.time()}
    storage.append(json_object)


def start_recording(file_name, record_every):
    print("Hold right click for more than 2 seconds (and then release) to end the recording for mouse and click 'esc' to end the recording for keyboard (both are needed to finish recording)")
    global name_of_recording
    name_of_recording = file_name

    global record_all
    record_all = record_every

    global keyboard_listener
    keyboard_listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release
    )

    global mouse_listener
    mouse_listener = mouse.Listener(
        on_click=on_click,
        on_scroll=on_scroll,
        on_move=on_move
    )

    keyboard_listener.start()
    mouse_listener.start()
    keyboard_listener.join()
    mouse_listener.join()