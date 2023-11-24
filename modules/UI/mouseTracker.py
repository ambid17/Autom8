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

        self.application.mouse_button = tk.Button(self.application.buttonBar, width=25, height=5, command=self.track_mouse, background="green", text="track")
        self.application.mouse_button.grid(row = 4, column = 2, pady = 2)

        self.application.master_screen = tk.Toplevel(self.application.root)
        self.application.master_screen.withdraw()
        self.application.master_screen.attributes("-transparent", "maroon3")

        self.application.picture_frame = tk.Frame(self.application.master_screen, background="maroon3")
        self.application.picture_frame.pack(fill=tk.BOTH, expand=tk.YES)

        self.is_tracking = False

    def track_mouse(self):
        self.is_tracking = not self.is_tracking
        button_text = "stop" if self.is_tracking else "track" 
        background = "red" if self.is_tracking else "green"
        self.application.mouse_button.config(text=button_text, background=background)
        
        if self.is_tracking:
            self.create_screen()
        else:
            self.remove_screen()

    def create_screen(self):
        # bring the master_screen back to the view
        self.application.master_screen.deiconify()
        # hide the root
        #self.application.root.withdraw()

        self.application.track_surface = tk.Canvas(self.application.picture_frame, cursor="cross", bg="grey11")
        self.application.track_surface.pack(fill=tk.BOTH, expand=tk.YES)

        self.application.master_screen.attributes('-fullscreen', True)
        self.application.master_screen.attributes('-alpha', 0.1)
        self.application.master_screen.lift()
        self.application.master_screen.attributes("-topmost", True)
        self.mouse_move_fnc_id = self.application.master_screen.bind("<Motion>", self.on_mouse_move)


    def remove_screen(self):
        self.application.track_surface.unbind("<Motion>", self.mouse_move_fnc_id)
        self.application.track_surface.destroy()
        self.application.master_screen.withdraw()
        self.application.root.deiconify()

    def on_mouse_move(self, e):
        x= e.x
        y= e.y

        pixel = pyautogui.pixel(x,y)
        text = f'{x},{y} / {pixel}'
        self.mouse_entry_var.set(text)
