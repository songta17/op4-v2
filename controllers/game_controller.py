"""Define the game controller."""
from typing import List 
import time

from controllers.tournament_controller import TournamentController
from controllers.player_controller import PlayerController
from controllers.round_controller import RoundController

from views.menu_views import MenuViews
from views.tournament_views import TournamentViews
from views.player_views import PlayerViews


class GameController:
    """Game controller."""

    def __init__(self):
        """Init Game Controller."""
        self.view = MenuViews
        self.tournament = None
        self.players = []
        self.current_round = 1
        # self.database = Database

    def main_menu(self):
        """Main Menu sequence."""
        self.view.app_title()
        self.view.terminal_clearing()
        self.view.app_title()
        self.view.menu_title()
        self.view.menu_list()
        self.main_menu_input()

    def main_menu_input(self):
        """Manage Input's admin choice on the main menu."""
        print("------------------")
        print(f"Current tournament : {self.tournament}.")
        print("------------------")
        print(f"Current players : {self.players}.")
        print("------------------")

        self.view.prompt_for_command_menu()
        user_input = input()
        self.view.terminal_clearing()

        if user_input == "1":
            self.tournament = TournamentController(TournamentViews).tournament_creation()
        elif user_input == "2":
            self.players = PlayerController(PlayerViews).add_player()
        elif user_input == "3":
            print("launch the pairs of players generator.")
            self.current_round = RoundController(self.current_round, self.players).generate()
        elif user_input == "4":
            print("Add results sections.")
        elif user_input == "5":
            print("Add a tournament description's.")
        elif user_input == "6":
            print("Save a tournament.")
        elif user_input == "7":
            print("Load a tounament.")
        elif user_input == "8":
            print("The Chess Tournament Memories App shutting. Please wait.")
            time.sleep(2)
            self.view.terminal_clearing()
            quit()
        else: 
            print("\nInput error : Select a valid option.")
            self.main_menu_input()
        return self.main_menu()
