"""Define the game controller."""
import time
from pprint import pprint

from controllers.tournament_controller import TournamentController
from controllers.player_controller import PlayerController
from controllers.round_controller import RoundController
from controllers.match_controller import MatchController

from views.menu_views import MenuViews
from views.tournament_views import TournamentViews

from models.database import Database
from models.tournament import Tournament


class GameController:
    """Game controller."""

    def __init__(self):
        """Init Game Controller."""
        self.view = MenuViews
        self.tournament = None
        self.round_list = []
        self.database = Database()

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
        pprint(self.tournament)
        db = self.database

        self.view.prompt_for_command_menu()
        user_input = input()
        self.view.terminal_clearing()

        if user_input == "1":
            self.tournament = TournamentController(db).new()
        elif user_input == "2":
            self.tournament['players_list'] = PlayerController(db).add_player()
            # self.tournament['players_list'] = [{'dob': '',
            #        'firstname': 'LIN',
            #        'lastname': 'JO',
            #        'national_id': '1',
            #        'opponents': [],
            #        'score': 10},
            #       {'dob': '',
            #        'firstname': 'CARTON',
            #        'lastname': 'JAMES',
            #        'national_id': '2',
            #        'opponents': [],
            #        'score': 2},
            #       {'dob': '',
            #        'firstname': 'MOUSSE',
            #        'lastname': 'MIKEY',
            #        'national_id': '3',
            #        'opponents': [],
            #        'score': 8},
            #       {'dob': '',
            #        'firstname': 'GUELLEE',
            #        'lastname': 'ROSS',
            #        'national_id': '4',
            #        'opponents': [],
            #        'score': 8},
            #       {'dob': '6',
            #        'firstname': 'LOI,',
            #        'lastname': 'RQCHE',
            #        'national_id': '5',
            #        'opponents': [],
            #        'score': 9},
            #       {'dob': '',
            #        'firstname': 'JUKL',
            #        'lastname': 'MINOCQ',
            #        'national_id': '6',
            #        'opponents': [],
            #        'score': 3},
            #       {'dob': '',
            #        'firstname': 'MOR',
            #        'lastname': 'CONS',
            #        'national_id': '7',
            #        'opponents': [],
            #        'score': 10},
            #       {'dob': '',
            #        'firstname': 'OUI',
            #        'lastname': 'BEN',
            #        'national_id': '8',
            #        'opponents': [],
            #        'score': 4}]
        elif user_input == "3":
            self.tournament['round_list'].append(RoundController(db).generate(
                self.tournament['current_round'],
                self.tournament['players_list']
            ))
        elif user_input == "4":
            self.tournament['round_list'] = MatchController(db).add_result(self.tournament['round_list'], self.tournament['current_round'] - 1)
            self.tournament['players_list'] = RoundController.update_score(self.tournament, self.tournament['current_round'])
            self.tournament['current_round'] = RoundController.update_round(self.tournament['current_round'])
        elif user_input == "5":
            self.tournament['description'] = TournamentViews.add_description()
            db.create_tournament_db(self.tournament)
        elif user_input == "6":
            db.create_tournament_db(self.tournament)
            time.sleep(2)
        elif user_input == "7":
            # input = TournamentViews.load_number_id
            # load = self.database.load_tournament_db(input)
            # self.tournament = load
            pass
        elif user_input == "9":
            print("The Chess Tournament Memories App shutting. Please wait.")
            time.sleep(2)
            self.view.terminal_clearing()
            quit()
        else:
            print("\nInput error : Select a valid option.")
            self.main_menu_input()
        return self.main_menu()
