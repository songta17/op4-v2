"""Menu Views."""

import os


class MenuViews:
    """Implement the view."""

    # def __init__(self):
    #     """Init the view."""
    #     pass

    @staticmethod
    def app_title():
        print("---------------------------------")
        print("--- Chess Tournament Memories ---")
        print("---------------------------------\n")

    @staticmethod
    def menu_title():
        print("------------- MENU --------------\n")

    @staticmethod
    def menu_list():
        """Show the menu list."""
        print("[1] - Create a new tournament.")
        print("[2] - Add 8 players.")
        print("[3] - Generate pairs of players.")
        print("[4] - Add results.")        
        print("[5] - Add a tournament description's.")
        print("[6] - Save a tournament.")        
        print("[7] - Load a tounament.")        
        print("[8] - Generate reports.")
        print("[9] - Quit the App.")
        print("\n")
        # # create a tournament
        # print("[1] - Create a tournament.")
        # # see tournament
        # print("[2] - See the tournament.")
        # # add number of player
        # print("[3] - Add a player.")
        # # see player
        # print("[4] - See players list.")
        # # select a pair of two random opponents for the first round
        # print("[5] - Generate a pair of two random opponents.")
        # # when match done, add a result
        # print("[6] - Add manually the result.")
        # # see result

    @staticmethod
    def prompt_for_command_menu():
        """Ask for the menu choice."""

        print("\nPlease select your choice: ")
        print(">", end ='')

    @staticmethod
    def terminal_clearing():
        os.system('clear')

    @staticmethod
    def add_player_title_section():
        """Show the add player title section."""

        print("----------------------------------------")
        print("Fill the form to add a player:          ")
        print("----------------------------------------\n")

    @staticmethod
    def prompt_lastname(number):
        """Ask lastname."""
        print(f"\nPlease type the lastname for the player {number}.")
        print(">", end ='')

    @staticmethod
    def prompt_firstname(number):
        """Ask firstname."""
        print(f"\nPlease type the firstname for the player {number}.")
        print(">", end ='')

    @staticmethod
    def prompt_birthday(number):
        """Ask birthday."""
        print(f"\nPlease type the birthday for the player {number}.")
        print(">", end ='')

    @staticmethod
    def prompt_gender(number):
        """Ask gender."""
        print(f"\nPlease type the gender for the player {number}.")
        print(">", end ='')

    @staticmethod
    def prompt_rank(number):
        """Ask rank."""
        print(f"\nPlease type the rank for the player {number}.")
        print(">", end ='')

    @staticmethod
    def redirect_to_menu_msg():
        """Redirect message to the menuc."""
        print("You will quickly be redirected to the Menu page...")

