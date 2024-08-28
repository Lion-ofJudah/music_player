import tkinter as ttk


class Controls:
    def __init__(self, parent):
        self.parent = parent

    def icon_button(self, icon: ttk.PhotoImage, command=lambda: None):
        """
        This method creates a button where the background and the border are removed.
            :param icon: tkinter PhotoImage
            :param command: function (optional)
            :return: tkinter button object
        """
        button = ttk.Button(self.parent, text="It exists", image=icon, command=command)
        button.config(relief=ttk.FLAT, borderwidth=0)

        return button
