"""Define the tournament controller."""
import time

from models.tournament import Tournament
from models.database import Database

from views.menu_views import MenuViews
from views.tournament_views import TournamentViews


class TournamentController: 

    def __init__(self, view):
            self.view = view 

    def tournament_creation(self):
        self.view.new_tournament_title_section()
        name_input = self.view.prompt_tournament_name()
        place_input = self.view.prompt_tournament_place()
        start_date_input = self.view.prompt_tournament_start_date()
        end_date_input = self.view.prompt_tournament_end_date()
        # round_list_input = TournamentViews.prompt_tournament_round_list()        
        # players_list_input = TournamentViews.prompt_tournament_players_list()
        # time_control_input = TournamentViews.prompt_tournament_time_control()

        try:
            tournament = Tournament(
                name_input, 
                place_input, 
                start_date_input, 
                end_date_input #,
                # round_list_input,
                # players_list_input,
                # time_control_input
            )
            self.view.tournament_created_msg()
            database = Database() # dans le constructeur
            database.table_tournaments.insert(tournament.serialize_tournament())
            MenuViews.redirect_to_menu_msg()
            time.sleep(2)
            return tournament.serialize_tournament()
        except:
            self.view.error_create_tournament()
            time.sleep(2)
