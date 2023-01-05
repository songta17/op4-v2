"""Define player."""
from models.database import Database
import json
# from pprint import pprint


class Player:
    """Player class."""

    def __init__(self, national_id, lastname, firstname, dob):
        self.national_id = national_id
        self.lastname = lastname
        self.firstname = firstname
        self.dob = dob
        self.score = 0.0
        self.opponents = []

    def __repr__(self, *args, **kwargs):
        return str(vars(self))

    def to_JSON(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__))

    def increment_score(self, point):
        self.score += point 

    def add_opponent(self, opponent):
        self.opponents.append(opponent)

    def serialize_player(self):
        return {
            'national_id': self.national_id,
            'lastname': self.lastname,
            'firstname': self.firstname,
            'dob': self.dob,
            'score': self.score,
            'opponents': self.opponents
        }

    # TEST controller
    # def create_player_db(self):
    #     try:
    #         Database().table_players.insert(self.to_JSON())
    #         pprint(player.to_JSON())
    #     except:
    #         print('Error: Can\'t save this player.')

    # def update_player_db(self):
    #     pass

# TEST
# player = Player(
#     "AB01",
#     "Phou",
#     "Vora",
#     "14/01/79"
# )

# print(player)
# player.increment_score(1)
# print(player)
# player.increment_score(0.5)
# print(player)
# player.add_opponent("Miackel")
# print(player)
# player.create_player_db()
# haha = Database().players_db.insert(player.to_JSON())
# # database = Database()
# # database.players_db.insert(player.to_JSON())
# # pprint(database.players_db)
# pprint(haha)
# pprint(player.to_JSON())