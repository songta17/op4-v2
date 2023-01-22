import os
from tinydb import TinyDB
from views.database_views import DatabaseViews

DB_FILENAME = "db_chess_tournament_memories.json"
DIRECTORY = "./database"


class Database:
    """Database Model."""

    def __init__(self):
        """Init database."""
        if not os.path.exists(DIRECTORY):
            os.makedirs(DIRECTORY)

        self.database = TinyDB(f'./database/{DB_FILENAME}')
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

    def load_tournaments(self):
        """Load tournaments."""
        all_tournaments = self.table_tournaments.all()
        return all_tournaments

    def load_players(self):
        all_tournaments = self.table_tournaments.all()
        players = []
        for index in range(len(all_tournaments)):
            for i in range(8):
                players.append(all_tournaments[index]['players_list'][i])
        return players
