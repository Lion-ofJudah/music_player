import tkinter as tk
import tkinter.filedialog
import os
from core.player import Player


class Controls:
    def __init__(self, parent):
        self.parent = parent
        self.player = Player()
        self.is_music_playing = False
        self.play_pause_button = None
        self.file_path = None

    def icon_button(self, icon: tk.PhotoImage, command=lambda: None):
        """
        This method creates a button where the background and the border are removed.
            :param icon: tkinter PhotoImage
            :param command: function (optional)
            :return: tkinter button object
        """
        button = tk.Button(self.parent, image=icon, command=command)
        button.config(relief=tk.FLAT, borderwidth=0)

        return button

    def create_toggle_play_pause_button(
        self, play_icon: tk.PhotoImage, pause_icon: tk.PhotoImage
    ):
        """
        This method creates a play/pause button with toggle functionality.
            :param play_icon: tkinter PhotoImage
            :param pause_icon: tkinter PhotoImage
            :return: tkinter button object
        """
        self.play_pause_button = self.icon_button(
            icon=pause_icon, command=self.toggle_play_pause
        )
        self.play_icon = play_icon
        self.pause_icon = pause_icon

        return self.play_pause_button

    def toggle_play_pause(self):
        """
        This method toggles the play/pause state of the button.
        """
        if self.is_music_playing:
            self.play_pause_button.config(image=self.play_icon)
            self.player.pause()
            self.is_music_playing = False

        else:
            try:
                self.player.play(self.file_path.name)
                self.play_pause_button.config(image=self.pause_icon)
                self.is_music_playing = True
            except AttributeError:
                pass

    def open_file_explorer_button(
        self, file_icon: tk.PhotoImage, file_icon_active: tk.PhotoImage
    ):
        """
        This method creates a file explorer button.
            :param file_icon: tkinter PhotoImage
            :return: tkinter button object
        """
        self.file_icon_active = file_icon_active
        self.file_icon = file_icon

        self.file_explorer_button = self.icon_button(
            icon=self.file_icon, command=self.open_file_explorer
        )
        return self.file_explorer_button

    def open_file_explorer(self):
        """
        This method controls the opening of a file explorer and changes the song path accordingly.
        """
        self.file_explorer_button.config(image=self.file_icon_active)

        new_file_path = tkinter.filedialog.askopenfile(title="File manager")

        self.file_explorer_button.config(image=self.file_icon)

        if new_file_path is None:
            return

        self.file_path = new_file_path

        if self.is_music_playing:
            self.player.play(self.file_path.name)

        else:
            self.player.stop()
            self.toggle_play_pause()
