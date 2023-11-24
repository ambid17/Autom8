import tkinter as tk
from modules import utils

class Screenshot:
    def __init__(self, application):
        self.application = application
        self.application.snip_label = tk.Label(self.application.buttonBar, text="File Name:")
        self.application.snip_label.grid(row = 0, column=0, pady = 2)

        self.snip_var = tk.StringVar()
        self.application.snip_entry = tk.Entry(self.application.buttonBar, textvariable=self.snip_var)
        self.application.snip_entry.grid(row = 0, column=1, pady = 2)

        self.application.snip_Button = tk.Button(self.application.buttonBar, width=15, height=5, command=self.create_screen_canvas, background="green", text="screenshot")
        self.application.snip_Button.grid(row = 0, column = 2, pady = 2)

    def create_screen_canvas(self):
        self.application.master_screen.deiconify()
        self.application.master.withdraw()

        self.application.snip_surface = tk.Canvas(self.application.picture_frame, cursor="cross", bg="grey11")
        self.application.snip_surface.pack(fill=tk.BOTH, expand=tk.YES)

        self.application.snip_surface.bind("<ButtonPress-1>", self.on_button_press)
        self.application.snip_surface.bind("<B1-Motion>", self.on_snip_drag)
        self.application.snip_surface.bind("<ButtonRelease-1>", self.on_button_release)

        self.application.master_screen.attributes('-fullscreen', True)
        self.application.master_screen.attributes('-alpha', .3)
        self.application.master_screen.lift()
        self.application.master_screen.attributes("-topmost", True)

    def on_button_release(self, event):
        self.display_rectangle_position()

        start_x = 0
        start_y = 0
        end_x = 0
        end_y = 0

        if self.start_x <= self.current_x and self.start_y <= self.current_y:
            print("right down")
            start_x = self.start_x
            start_y = self.start_y
            end_x = self.current_x - self.start_x
            end_y = self.current_y - self.start_y
            

        elif self.start_x >= self.current_x and self.start_y <= self.current_y:
            print("left down")
            start_x = self.current_x
            start_y = self.start_y
            end_x = self.start_x - self.current_x
            end_y = self.current_y - self.start_y

        elif self.start_x <= self.current_x and self.start_y >= self.current_y:
            print("right up")
            start_x = self.start_x
            start_y = self.current_y
            end_x = self.current_x - self.start_x
            end_y = self.start_y - self.current_y

        elif self.start_x >= self.current_x and self.start_y >= self.current_y:
            print("left up")
            start_x = self.current_x
            start_y = self.current_y
            end_x = self.start_x - self.current_x
            end_y = self.start_y - self.current_y

        utils.take_bounded_screenshot(start_x, start_y,  end_x, end_y, self.snip_var.get())
        self.exit_screenshot_mode()
        return event

    def exit_screenshot_mode(self):
        self.application.snip_surface.destroy()
        self.application.master_screen.withdraw()
        self.application.master.deiconify()

    def on_button_press(self, event):
        # save mouse drag start position
        self.start_x = self.application.snip_surface.canvasx(event.x)
        self.start_y = self.application.snip_surface.canvasy(event.y)
        self.application.snip_surface.create_rectangle(0, 0, 1, 1, outline='red', width=3, fill="maroon3")

    def on_snip_drag(self, event):
        self.current_x, self.current_y = (event.x, event.y)
        # expand rectangle as you drag the mouse
        self.application.snip_surface.coords(1, self.start_x, self.start_y, self.current_x, self.current_y)

    def display_rectangle_position(self):
        print(self.start_x)
        print(self.start_y)
        print(self.current_x)
        print(self.current_y)