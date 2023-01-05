"""Define round."""


class Round:
    """Round model."""

    def __init__(self, round_name, matchs_list, start_time):
        """Init a round."""
        self.round_name = round_name
        self.matchs_list = matchs_list
        self.start_time = start_time
        self.end_time = None

    def __repr__(self):
        return str(vars(self))
