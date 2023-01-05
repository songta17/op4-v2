"""Define the tournament controller."""

import time

from models.player import Player
from views.player_views import PlayerViews
from views.menu_views import MenuViews


class PlayerController:
    """Player controller."""

    def __init__(self):
        self.players = []

    def add_player(self):
        """Add a player"""
        player_number = 1

        while player_number < 9:
            PlayerViews.add_player_title_section()
            national_id_input = PlayerViews.prompt_national_id()
            lastname_input = PlayerViews.prompt_lastname()
            firstname_input = PlayerViews.prompt_firstname()
            dob_input = PlayerViews.prompt_dob()
            player_number += 1

            try:
                player = Player(
                    national_id_input, 
                    lastname_input, 
                    firstname_input, 
                    dob_input
                )
                self.players.append(player)
                database = Database()
                database.table_players.insert(player.serialize_player())
                PlayerViews.player_added_msg(player_number - 1)
                time.sleep(1)
                MenuViews.terminal_clearing()
                
            except:
                PlayerViews.error_add_player()
                time.sleep(1)
            
        MenuViews.redirect_to_menu_msg()
        return self.players

        



        # try:
        #     player = Player(lastname, firstname, dob)
        #     print(f"\Player {lastname} {firstname} added!")
        #     print("You will quickly be redirected to the Menu page...")
        #     time.sleep(2)
        # except:
        #     print("\nAn error occured while trying to add a player.")
        #     time.sleep(2)
        #     # TournamentController.tournament_creation()






"""Define the tournament controller."""

import time

from models.tournament import Tournament
from models.database import Database
# from models.player import Player

from views.menu_views import MenuViews
from views.tournament_views import TournamentViews
# from controllers.game_controller import GameController


# class TournamentController: 

#     def __init__(self):
#         #     self.view = view
#         pass

#     def tournament_creation():
#         TournamentViews.new_tournament_title_section()
#         name_input = TournamentViews.prompt_tournament_name()
#         place_input = TournamentViews.prompt_tournament_place()
#         start_date_input = TournamentViews.prompt_tournament_start_date()
#         end_date_input = TournamentViews.prompt_tournament_end_date()
#         # round_list_input = TournamentViews.prompt_tournament_round_list()        
#         # players_list_input = TournamentViews.prompt_tournament_players_list()
#         # time_control_input = TournamentViews.prompt_tournament_time_control()

#         try:
#             tournament = Tournament(
#                 name_input, 
#                 place_input, 
#                 start_date_input, 
#                 end_date_input #,
#                 # round_list_input,
#                 # players_list_input,
#                 # time_control_input
#             )
#             TournamentViews.tournament_created_msg()
#             database = Database()
#             database.table_tournaments.insert(tournament.serialize_tournament())
#             MenuViews.redirect_to_menu_msg()
#             time.sleep(2)
#             return tournament.serialize_tournament()
#         except:
#             TournamentViews.error_create_tournament()
#             time.sleep(2)
#             # TournamentController.tournament_creation()
#             # TournamentController.tournament_creation()
#             # game = GameController()
#             # game.main_menu()

#     # def ask_for_input():
#     #     """Define the user input."""
#     #     user_input = input()

