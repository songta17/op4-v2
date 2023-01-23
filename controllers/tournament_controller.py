"""Define the tournament controller."""
import time

from views.menu_views import MenuViews
from models.tournament import Tournament
from views.tournament_views import TournamentViews


class TournamentController:

    def __init__(self, database):
        self.view = TournamentViews
        self.database = database

    def new(self):
        self.view.new_tournament_title_section()
        name_input = self.view.prompt_tournament_name()
        place_input = self.view.prompt_tournament_place()
        start_date_input = self.view.prompt_tournament_start_date()
        end_date_input = self.view.prompt_tournament_end_date()

        try:
            tournament = Tournament(
                name_input,
                place_input,
                start_date_input,
                end_date_input,
            )
            self.view.tournament_created_msg()
            MenuViews.redirect_to_menu_msg()
            time.sleep(2)
            return tournament.serialize_tournament()
        except Exception:
            self.view.error_create_tournament()
            time.sleep(2)
