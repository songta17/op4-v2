"""Define the database controller."""
import time

from views.database_views import DatabaseViews


class DatabaseController:

    def __init__(self, database):
        self.view = DatabaseViews
        self.database = database

    def save(self, tournament):
        self.view.database_title_section()
        self.view.saving_tournament()
        self.database.create_tournament_db(tournament)
        time.sleep(2)

    def load(self):
        self.view.database_title_section()
        self.database.show_ids()
        input_load = self.view.load_number_id()
        self.view.loading_tournament()
        time.sleep(2)
        return self.database.load_tournament_db(input_load)
