import tkinter as tk
from pynput import mouse
from main import Application

class MouseTracker:
    def __init__(self, application: Application):
        self.application = application
        self.application.mouse_label = tk.Label(self.application.buttonBar, text="Mouse Location:")
        self.application.mouse_label.grid(row = 4, column=0, pady = 2)

        self.mouse_entry_var = tk.StringVar()
        self.application.mouse_entry = tk.Entry(self.application.buttonBar, textvariable=self.mouse_entry_var)
        self.application.mouse_entry.grid(row = 4, column=1, pady = 2)

        self.application.mouse_Button = tk.Button(self.application.buttonBar, width=15, height=5, command=self.track_mouse, background="green", text="track")
        self.application.mouse_Button.grid(row = 4, column = 2, pady = 2)

        self.is_tracking = False

    def track_mouse(self):
        self.is_tracking = not self.is_tracking
        button_text = "stop" if self.is_tracking else "track" 
        background = "red" if self.is_tracking else "green"
        self.application.mouse_Button.config(text=button_text, background=background)
        
        if self.is_tracking:
            self.application.master.bind('<Motion>', self.on_mouse_move)
        else:
            self.application.master.unbind('<Motion>', self.on_mouse_move)

    def on_mouse_move(self, e):
        x= e.x
        y= e.y
        text = f'{x},{y}'
        self.mouse_entry_var.set(text)
