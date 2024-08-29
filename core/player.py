from ffpyplayer.player import MediaPlayer


class Player:
    def __init__(self):
        self.player = None

    def play(self, file_path: str):
        if self.player is None:
            self.player = MediaPlayer(file_path)

        elif self.player.get_pause():
            self.player.set_pause(False)

        else:
            self.player = MediaPlayer(file_path)

    def pause(self):
        if self.player is not None:
            self.player.set_pause(True)
