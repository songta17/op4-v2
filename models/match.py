"""Define match."""


class Match:
    """Match class."""

    def __init__(
            self,
            player_playing_in_white,
            player_playing_in_black,
            winner
            ):
        self.player_playing_in_white = player_playing_in_white
        self.player_playing_in_black = player_playing_in_black
        self.winner = winner

    def __repr__(self):
        return str(vars(self))

    # def win_match(self):
    #     """Add One point for the winner."""
    #     pass

    # def lose_match(self, name):
    #     pass

    # def draw_match(self):
    #     """Draw match give 0,5 point to two players."""
    #     pass
