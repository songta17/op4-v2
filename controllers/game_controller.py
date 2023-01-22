"""Define the game controller."""
import time
from pprint import pprint

from controllers.tournament_controller import TournamentController
from controllers.player_controller import PlayerController
from controllers.reports_controller import ReportsController
from controllers.round_controller import RoundController
from controllers.match_controller import MatchController
from controllers.database_controller import DatabaseController

from views.menu_views import MenuViews
from views.report_views import ReportViews
from views.tournament_views import TournamentViews

from models.database import Database


class GameController:
    """Game controller."""

    def __init__(self):
        """Init Game Controller."""
        self.view = MenuViews
        self.tournament = None
        self.round_list = []
        self.database = Database()
        self.step_access = True
        # self.report = ReportsController()

    def main_menu(self):
        """Main Menu sequence."""
        self.view = MenuViews
        self.view.run_menu()
        self.main_menu_input()

    def report_menu(self):
        """Main report sequence."""
        self.view = ReportViews
        self.view.run_report()
        self.main_report_input()

    def main_report_input(self):
        """Manage Input's admin choice on the report menu."""
        self.view.prompt_for_command_menu()
        user_input = input()
        self.view.terminal_clearing()
        if user_input == "1":
            self.view.report_players()
            tournaments = self.database.load_tournaments()
            # players = self.database.load_players_tournaments()
            # ReportsController().report_players_tournaments(players)
            ReportsController().report_players_tournaments(tournaments)
        elif user_input == "2":
            self.view.report_tournaments()
            tournaments = self.database.load_tournaments()
            ReportsController().generate_report_tournaments(tournaments)
        elif user_input == "3":
            self.view.report_tournament()
            ReportsController().generate_report_tournament(self.tournament)
        elif user_input == "4":
            self.view.report_tournament_players()
            ReportsController().generate_report_players(self.tournament['players_list'])
        elif user_input == "5":
            self.view.report_rounds_tournament()
            ReportsController().generate_report_rounds_tournament(self.tournament['round_list'])
        elif user_input == "8":
            self.main_menu()
        elif user_input == "9":
            self.view.quit_app()
        else:
            self.view.input_error()
            self.view.report_list()
            self.main_report_input()
        user_input = self.view.nav_back_or_quit()
        if user_input == "8":
            self.report_menu()
        elif user_input == "9":
            self.view.quit_app()

    def main_menu_input(self):
        """Manage Input's admin choice on the main menu."""
        # print(f"Current Tournament: {self.tournament['name']}")
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
        elif user_input == "3" and self.tournament['current_round'] < 5 and self.step_access:
            self.tournament['round_list'].append(RoundController(db).generate(
                self.tournament['current_round'],
                self.tournament['players_list']
            ))
            self.step_access = False
        elif user_input == "4"  and self.tournament['current_round'] < 5 and not self.step_access:
            self.tournament['round_list'] = MatchController(db).add_result(self.tournament['round_list'], self.tournament['current_round'] - 1)
            self.tournament['players_list'] = RoundController.update_score(self.tournament, self.tournament['current_round'])
            self.tournament['current_round'] = RoundController.update_round(self.tournament['current_round'])
            self.step_access = True
        elif user_input == "5":
            self.tournament['description'] = TournamentViews.add_description()
        elif user_input == "6":
            DatabaseController(db).save(self.tournament)
        elif user_input == "7":
            self.tournament = DatabaseController(db).load()
            pass
        elif user_input == "8":
            self.report_menu()
        elif user_input == "9":
            self.view.quit_app()
        else:
            self.view.input_error()
            self.main_menu_input()
        return self.main_menu()
