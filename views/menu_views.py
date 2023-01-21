"""Menu Views."""
import time
import os


class MenuViews:
    """Implement the view."""

    def run_menu():
        MenuViews.app_title()
        MenuViews.terminal_clearing()
        MenuViews.app_title()
        MenuViews.menu_title()
        MenuViews.menu_list()

    def app_title():
        print("--------------------------------------")
        print("----- Chess Tournament Memories ------")
        print("--------------------------------------\n")

    def menu_title():
        print("# MENU\n")

    def menu_list():
        """Show the menu list."""
        print("[1] - Create a new tournament.")
        print("[2] - Add 8 players.")
        print("[3] - Generate pairs of players.")
        print("[4] - Add results.")
        print("[5] - Add a tournament description's.")
        print("[6] - Save a tournament.")
        print("[7] - Load a tounament.")
        print("[8] - See reports.")
        print("[9] - Quit the App.")

    def prompt_for_command_menu():
        """Ask for the menu choice."""
        print("\nPlease select your choice: ")
        print("> ", end="")

    def terminal_clearing():
        os.system('clear')

    def add_player_title_section():
        """Show the add player title section."""
        print("----------------------------------------")
        print("Fill the form to add a player:          ")
        print("----------------------------------------\n")

    def prompt_lastname(number):
        """Ask lastname."""
        print(f"\nPlease type the lastname for the player {number}.")
        print("> ", end="")

    def prompt_firstname(number):
        """Ask firstname."""
        print(f"\nPlease type the firstname for the player {number}.")
        print("> ", end="")

    def prompt_birthday(number):
        """Ask birthday."""
        print(f"\nPlease type the birthday for the player {number}.")
        print("> ", end="")

    def prompt_gender(number):
        """Ask gender."""
        print(f"\nPlease type the gender for the player {number}.")
        print("> ", end="")

    def prompt_rank(number):
        """Ask rank."""
        print(f"\nPlease type the rank for the player {number}.")
        print("> ", end="")

    def redirect_to_menu_msg():
        """Redirect message to the menuc."""
        print("You will quickly be redirected to the Menu page...")

    def quit_app():
        print("The Chess Tournament Memories App shutting. Please wait.")
        time.sleep(2)
        MenuViews.terminal_clearing()
        quit()

    def input_error():
        print("\nInput error : Select a valid option.")

    def nav_back_or_quit():
        print("Reports List [8] / Main Menu [9]")
        print("> ", end="")
        return input()
