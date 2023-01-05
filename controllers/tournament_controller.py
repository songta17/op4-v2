"""Define the tournament controller."""

import time

from models.tournament import Tournament
from models.database import Database
# from models.player import Player

from views.menu_views import MenuViews
from views.tournament_views import TournamentViews
# from controllers.game_controller import GameController


class TournamentController: 

    def __init__(self):
        #     self.view = view
        pass

    def tournament_creation():
        TournamentViews.new_tournament_title_section()
        name_input = TournamentViews.prompt_tournament_name()
        place_input = TournamentViews.prompt_tournament_place()
        start_date_input = TournamentViews.prompt_tournament_start_date()
        end_date_input = TournamentViews.prompt_tournament_end_date()
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
            TournamentViews.tournament_created_msg()
            database = Database()
            database.table_tournaments.insert(tournament.serialize_tournament())
            MenuViews.redirect_to_menu_msg()
            time.sleep(2)
            return tournament.serialize_tournament()
        except:
            TournamentViews.error_create_tournament()
            time.sleep(2)
            # TournamentController.tournament_creation()
            # TournamentController.tournament_creation()
            # game = GameController()
            # game.main_menu()

    # def ask_for_input():
    #     """Define the user input."""
    #     user_input = input()

