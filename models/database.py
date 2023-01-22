import os
from tinydb import TinyDB
from pprint import pprint
from views.database_views import DatabaseViews
# from time import sleep
# import json

DB_FILENAME = "db_chess_tournament_memories.json"
DIRECTORY = "./database"


class Database:
    """Database Model."""

    def __init__(self):
        """Init database."""
        if not os.path.exists(DIRECTORY):
            os.makedirs(DIRECTORY)

        self.database = TinyDB(f'./database/{DB_FILENAME}')
        self.table_players = self.database.table('players')
        self.table_tournaments = self.database.table('tournaments')

    def __repr__(self, *args, **kwargs):
        return str(vars(self))

    def create_tournament_db(self, tournament):
        """save tournament"""
        self.table_tournaments.insert(tournament)

    def load_tournament_db(self, id):
        """Load tournament"""
        all_tournaments = self.table_tournaments.all()
        tournaments = []
        for tournament in all_tournaments:
            tournaments.append(tournament)
            DatabaseViews.show_tournaments_ids(tournaments)
        return tournaments[int(id)]

    def show_ids(self):
        DatabaseViews.tournament_list_ids()
        all_tournaments = self.table_tournaments.all()
        for id in range(len(all_tournaments)):
            DatabaseViews.show_id_printer(id, all_tournaments[int(id)]['name'])

    # def load_tournaments(self):
    #     """Load all tournaments."""
    #     all_tournaments = self.table_tournaments.all()
    #     tournaments = []
    #     for tournament in all_tournaments:
    #         tournaments.append(tournament)
    #         DatabaseViews.show_tournaments_ids(tournaments)
    #     return tournaments[int(id)]
    
    def load_tournaments(self):
        """Load tournaments."""
        all_tournaments = self.table_tournaments.all()
        return all_tournaments

    def load_players_tournaments(self):
        all_tournaments = self.table_tournaments.all()
        players = []
        for index in range(len(all_tournaments)):
            players.append(all_tournaments[index]['players_list'])
        return players


    # .search(where('field') == 'value')
    # def create_player_db(self):
    #     try:
    #         Database().table_players.insert(self.to_JSON())
    #         pprint(player.to_JSON())
    #     except:
    #         print('Error: Can\'t save this player.')

    # def update_player_db(self):
    #     pass

    # def to_JSON(self):
    #     return json.loads(json.dumps(self, default=lambda o: o.__dict__))

    # def update_opponents_player(self, opponent):
    #     new_opponents = self.players_db.opponents.append(opponent)
    #     breakpoint()
    #     self.players_db.update(
    #         {
    #         'opponents': new_opponents
    #         }, self.players_db.national_id == 'ABB1001')

    # def insert_player(self):
    #     self.database.table('players')
    #     self.database.insert({"coucou" : 'haha'})
    #     # self.database.table('players')
    #     print("haha")


# database = Database()
# database.players_db.insert(
#     {
#         'national_id': 'ABB1001',
#         'lastname': 'Connor',
#         'firstname': 'John',
#         'dob': '01/01/1979',
#         'score': '0.0',
#         'opponents': ["sarah", "t1"]
#     }
# )
# pprint(database.players_db.all())
# sleep(5)
# database.players_db.update_opponents_player("C17")
# pprint(database.players_db.all())
