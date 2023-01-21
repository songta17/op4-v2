"""Define match."""


class Match:
    """Match class."""

    def __init__(
            self,
            player_1,
            player_1_name,
            player_2,
            player_2_name
            ):
        self.player_1 = player_1
        self.player_2 = player_2
        self.player_1_name = player_1_name
        self.player_2_name = player_2_name
        self.score_player_1 = None
        self.score_player_2 = None

    def serialize_match(self):
        return {
            'player_1': self.player_1,
            'player_1_name': self.player_1_name,
            'score_player_1': self.score_player_1,
            'player_2': self.player_2,
            'player_2_name': self.player_2_name,
            'score_player_2': self.score_player_2
        }
