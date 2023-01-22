"""Define tournament."""


class Tournament:
    """Tournament class."""

    def __init__(
            self,
            name,
            place,
            start_date,
            end_date=None,
            round_list=[],
            players_list=[],
            current_round=1,
            round_number=4,
            description=None
            ):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.current_round = current_round
        self.round_list = round_list
        self.players_list = players_list
        self.round_number = round_number
        self.description = description

    def __repr__(self, *args, **kwargs):
        return str(vars(self))

    def add_player(self, new_player):
        self.players_list.append(new_player)

    def add_round(self, new_round):
        self.players_list.append(new_round)

    def edit_description(self, new_description):
        self.description = new_description

    def serialize_tournament(self):
        return {
            'name': self.name,
            'place': self.place,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'current_round': self.current_round,
            'round_list': self.round_list,
            'players_list': self.players_list,
            'round_number': self.round_number,
            'description': self.description
        }
