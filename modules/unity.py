import pyautogui
import time

def openUnityWorkspace():
    print("opening unity stuff")

    pyautogui.press('win')
    time.sleep(0.5)
    pyautogui.write('unity')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)

    pyautogui.press('win')
    time.sleep(0.5)
    pyautogui.write('visual')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)