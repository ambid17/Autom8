import pyautogui
import keyboard
import mouse
import time
import datetime

def trackMousePos():
    while keyboard.is_pressed('q') == False:
        pos = pyautogui.position()
        print(pos)
        time.sleep(0.5)


def clickImageCenter(image_name):
    image_center = pyautogui.locateCenterOnScreen(image_name)
    print(image_center)
    pyautogui.click(image_center.x, image_center.y)

def take_bounded_screenshot(x1, y1, x2, y2):
    image = pyautogui.screenshot(region=(int(x1), int(y1), int(x2), int(y2)))
    file_name = datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
    image.save("screenshots/" + file_name + ".png")