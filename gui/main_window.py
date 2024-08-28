import tkinter as ttk
from config.config import Config


class MainWindow(ttk.Tk):
    def __init__(self):
        super().__init__()
        self.title(Config.APP_NAME)

    def run(self):
        self.mainloop()
