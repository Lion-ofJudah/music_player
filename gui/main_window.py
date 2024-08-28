import tkinter as ttk
import os
from config.config import Config
from gui.controls import Controls


class MainWindow(ttk.Tk):
    def __init__(self):
        super().__init__()
        self.title(Config.APP_NAME)
        self.controls = Controls(self)
        self.play_icon = None
        self.create_widgets()

    def create_widgets(self):
        """
        Method which creates widgets on the main window of the music player application.
        """
        self.play_icon = ttk.PhotoImage(file=os.path.abspath("./assets/icons/play.png"))
        play_button = self.controls.icon_button(icon=self.play_icon)

        play_button.pack()

    def run(self):
        self.mainloop()
