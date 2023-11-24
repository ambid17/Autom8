import tkinter as tk
from pynput import mouse
from main import Application
import pyautogui

class MouseTracker:
    def __init__(self, application: Application):
        self.application = application
        self.application.mouse_label = tk.Label(self.application.buttonBar, text="mouse x,y / r,g,b:")
        self.application.mouse_label.grid(row = 4, column=0, pady = 2)

        self.mouse_entry_var = tk.StringVar()
        self.application.mouse_entry = tk.Entry(self.application.buttonBar, textvariable=self.mouse_entry_var)
        self.application.mouse_entry.grid(row = 4, column=1, pady = 2)

        self.application.mouse_button = tk.Button(self.application.buttonBar, width=15, height=5, command=self.track_mouse, background="green", text="track")
        self.application.mouse_button.grid(row = 4, column = 2, pady = 2)

        self.is_tracking = False
        self.mouse_listener = []

    def track_mouse(self):
        if self.is_tracking:
            self.stop_waiting_for_click()

        self.update_button()
        
        if self.is_tracking:
            self.wait_for_click()
        else:
            self.stop_waiting_for_click()

    def wait_for_click(self):
        self.mouse_listener = mouse.Listener(
            on_click=self.on_click,
        )

        self.mouse_listener.start()

    def stop_waiting_for_click(self):
        self.mouse_listener.stop()
        
    def on_click(self, x, y, button, pressed):
        self.update_button()
        pixel = pyautogui.pixel(x,y)
        text = f'{x},{y} / {pixel}'
        print(text)
        self.mouse_entry_var.set(text)
        self.mouse_listener.stop()
        return False
    
    def update_button(self):
        self.is_tracking = not self.is_tracking
        button_text = "stop" if self.is_tracking else "track" 
        background = "red" if self.is_tracking else "green"
        self.application.mouse_button.config(text=button_text, background=background)
