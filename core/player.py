from ffpyplayer.player import MediaPlayer


class Player:
    def __init__(self):
        self.player = None

    def play(self, file_path: str):
        """
        This method controls music play.
            :param file_path: string file path name
        """
        if self.player is None:
            self.player = MediaPlayer(file_path)

        elif self.player.get_pause():
            self.player.set_pause(False)

        else:
            self.player = MediaPlayer(file_path)

    def pause(self):
        """
        This method pauses a song if it is playing.
        """
        if self.player is not None:
            self.player.set_pause(True)

    def stop(self):
        """
        This method stops a song completely.
        """
        if self.player is not None:
            self.player.close_player()
            self.player = None
