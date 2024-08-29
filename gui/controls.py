import tkinter as tk


class Controls:
    def __init__(self, parent):
        self.parent = parent
        self.is_music_playing = False
        self.play_pause_button = None

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
        self, play_icon: tk.PhotoImage, pause_icon: tk.PhotoImage, command=lambda: None
    ):
        """
        This method creates a play/pause button with toggle functionality.
            :param play_icon: tkinter PhotoImage
            :param pause_icon: tkinter PhotoImage
            :param command: function (optional)
        """
        self.play_pause_button = self.icon_button(
            icon=pause_icon, command=lambda: self.toggle_play_pause(command=command)
        )
        self.play_icon = play_icon
        self.pause_icon = pause_icon

        return self.play_pause_button

    def toggle_play_pause(self, command):
        """
        This method toggles the play/pause state of the button
        """
        if self.is_music_playing:
            self.play_pause_button.config(image=self.play_icon)
            self.is_music_playing = False

        else:
            self.play_pause_button.config(image=self.pause_icon)
            self.is_music_playing = True

        command()
