def get_current_pts_and_duration(player):
    """
    This function returns the current audio time and the total duration of the music.
        :param player: Media Player
        :return: tuple(current_pts (float), duration (float))
    """
    try:
        current_pts = round(player.player.get_pts(), 2)
        duration = round(player.player.get_metadata().get("duration", 0), 2)

    except AttributeError:
        current_pts = 0
        duration = 0

    return current_pts, duration
