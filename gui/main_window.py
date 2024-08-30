import tkinter as tk
import os
from config.config import Config
from gui.controls import Controls
from gui.utils import resized_img


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(Config.APP_NAME)
        self.controls = Controls(self)

        self.play_icon = resized_img(os.path.abspath("./assets/icons/play.png"), 64, 64)
        self.pause_icon = resized_img(
            os.path.abspath("./assets/icons/pause.png"), 64, 64
        )
        self.file_icon = resized_img(
            os.path.abspath("./assets/icons/folder.png"), 64, 64
        )
        self.file_icon_active = resized_img(
            os.path.abspath("./assets/icons/folder_active.png"), 64, 64
        )

        self.create_widgets()

    def create_widgets(self):
        """
        Method which creates widgets on the main window of the music player application.
        """
        file_explorer_button = self.controls.open_file_explorer_button(
            file_icon=self.file_icon, file_icon_active=self.file_icon_active
        )
        file_explorer_button.pack()
        play_pause_button = self.controls.create_toggle_play_pause_button(
            play_icon=self.play_icon, pause_icon=self.pause_icon
        )
        play_pause_button.pack()

    def run(self):
        """
        This method runs the window.
        """
        self.mainloop()
