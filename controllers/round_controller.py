"""Define the round controller."""
import time
from datetime import datetime

from models.round import Round
from views.round_views import RoundViews
from views.menu_views import MenuViews


class RoundController:
    """Player controller."""

    def __init__(self, current_round, players_list):
        self.current_round = current_round
        self.players_list = players_list
        self.round_list = []

    def generate(self):
        """Add a player"""

        # [
        #     {'national_id': 'zefr', 'lastname': 'efrd', 'firstname': 'rgdf', 'dob': 'efrd', 'score': 0.0, 'opponents': []}, 
        #     {'national_id': 'ppp', 'lastname': 'ppp', 'firstname': 'ppp', 'dob': 'p', 'score': 0.0, 'opponents': []}, 
        #     {'national_id': 'pkyth', 'lastname': 'hby', 'firstname': 'nyht', 'dob': 'ntg', 'score': 0.0, 'opponents': []}, 
        #     {'national_id': 'byt', 'lastname': 'hbbybbt', 'firstname': 'bb', 'dob': 'yfb', 'score': 0.0, 'opponents': []}, 
        #     {'national_id': 'bbyh', 'lastname': 'byb', 'firstname': 'g', 'dob': 'y', 'score': 0.0, 'opponents': []}, 
        #     {'national_id': 'hb', 'lastname': 'ygbb', 'firstname': 'ygb', 'dob': 'ygbb', 'score': 0.0, 'opponents': []}, 
        #     {'national_id': 'ygb', 'lastname': 'yg', 'firstname': 'b', 'dob': 't', 'score': 0.0, 'opponents': []}, 
        #     {'national_id': 'g', 'lastname': 'gt', 'firstname': 'gt', 'dob': 'gt', 'score': 0.0, 'opponents': []}
        # ]
        round_name = "Round " + str(self.current_round)
        matchs_list = []
        start_time = datetime.now() 
        # 2022-12-27 08:26:49.219717

        try: 
            round = Round(
                round_name,
                matchs_list,
                start_time
            )
            breakpoint()
            matchs_list.append(round)
            time.sleep(10)
            MenuViews.redirect_to_menu_msg()
        except:
            print("error save round")
            time.sleep(3)
            MenuViews.redirect_to_menu_msg()

        # generate_match
        #######################
        # generate les 4 match
        #######################
        # player_playing_in_white
        # player_playing_in_black
        # winner

        # while player_number < 9:
        #     PlayerViews.add_player_title_section()
        #     national_id_input = PlayerViews.prompt_national_id()
        #     lastname_input = PlayerViews.prompt_lastname()
        #     firstname_input = PlayerViews.prompt_firstname()
        #     dob_input = PlayerViews.prompt_dob()
        #     player_number += 1

        #     try:
        #         player = Player(
        #             national_id_input, 
        #             lastname_input, 
        #             firstname_input, 
        #             dob_input
        #         )
        #         self.players.append(player)
        #         database = Database()
        #         database.table_players.insert(player.serialize_player())
        #         PlayerViews.player_added_msg(player_number - 1)
        #         time.sleep(1)
        #         MenuViews.terminal_clearing()
                
        #     except:
        #         PlayerViews.error_add_player()
        #         time.sleep(1)
            
        # MenuViews.redirect_to_menu_msg()
        # return self.players

    # def add_player(self):
    #     """Add a player"""
    #     player_number = 1

    #     while player_number < 9:
    #         PlayerViews.add_player_title_section()
    #         national_id_input = PlayerViews.prompt_national_id()
    #         lastname_input = PlayerViews.prompt_lastname()
    #         firstname_input = PlayerViews.prompt_firstname()
    #         dob_input = PlayerViews.prompt_dob()
    #         player_number += 1

    #         try:
    #             player = Player(
    #                 national_id_input, 
    #                 lastname_input, 
    #                 firstname_input, 
    #                 dob_input
    #             )
    #             self.players.append(player)
    #             database = Database()
    #             database.table_players.insert(player.serialize_player())
    #             PlayerViews.player_added_msg(player_number - 1)
    #             time.sleep(1)
    #             MenuViews.terminal_clearing()
                
    #         except:
    #             PlayerViews.error_add_player()
    #             time.sleep(1)
            
    #     MenuViews.redirect_to_menu_msg()
    #     return self.players
