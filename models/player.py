"""Define player."""
import json
import random


class Player:
    """Player class."""

    def __init__(self, national_id, lastname, firstname, dob):
        self.national_id = national_id
        self.lastname = lastname
        self.firstname = firstname
        self.dob = dob
        self.score = 0.0 # random.randint(0, 10)  # 0.0
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
