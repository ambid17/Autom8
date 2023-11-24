import cv2 as cv
import tkinter as tk


# yoinked from: https://stackoverflow.com/questions/49901928/how-to-take-a-screenshot-with-python-using-a-click-and-drag-method-like-snipping
class Application:
    def __init__(self, master: tk.Tk):
        self.snip_surface = None
        self.master = master
        self.start_x = None
        self.start_y = None
        self.current_x = None
        self.current_y = None
        self.is_tracking_mouse = False

        self.master.geometry('600x800+200+200')  # set new geometry
        self.master.title('Autom8')

        self.menu_frame = tk.Frame(master)
        self.menu_frame.pack(fill=tk.BOTH, expand=tk.YES, padx=1, pady=1)

        self.buttonBar = tk.Frame(self.menu_frame, bg="")
        self.buttonBar.pack()

        from modules.UI import screenshot
        self.screenshot = screenshot.Screenshot(self)

        from modules.UI import record
        self.record = record.Record(self)

        from modules.UI import playRecording
        self.play_recording = playRecording.PlayRecording(self)

        from modules.UI import trimps
        self.trimps = trimps.Trimps(self)

        from modules.UI import mouseTracker
        self.mouse_tracker = mouseTracker.MouseTracker(self)

if __name__ == '__main__':
    print(cv.__version__)
    root = tk.Tk()
    app = Application(root)
    root.mainloop()

    

