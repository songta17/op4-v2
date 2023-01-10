"""Define the tournament controller."""

import time

from models.player import Player
from views.menu_views import MenuViews


class PlayerController:
    """Player controller."""

    def __init__(self, view):
        """Init the player controller."""
        self.view = view
        self.players = []

    def add_player(self):
        """Add a player"""
        player_number = 1

        while player_number < 9:
            self.view.add_player_title_section()
            national_id_input = self.view.prompt_national_id()
            lastname_input = self.view.prompt_lastname()
            firstname_input = self.view.prompt_firstname()
            dob_input = self.view.prompt_dob()
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
                self.view.player_added_msg(player_number - 1)
                time.sleep(1)
                MenuViews.terminal_clearing()
                
            except:
                self.view.error_add_player()
                time.sleep(1)
            
        MenuViews.redirect_to_menu_msg()
        return self.players
