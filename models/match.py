"""Define match."""


class Match:
    """Match class."""

    def __init__(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two

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