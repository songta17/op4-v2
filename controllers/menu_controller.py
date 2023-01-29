"""Define the game controller."""

import time

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


class MenuController:
    """Game controller."""

    def __init__(self):
        """Init Game Controller."""
        self.view = MenuViews
        self.tournament = None
        self.round_list = []
        self.step_access = True
        self.database = Database()
        self.report = ReportsController()

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
            players = self.database.load_players()
            ReportsController().report_players_tournaments(players)
        elif user_input == "2":
            self.view.report_tournaments()
            tournaments = self.database.load_tournaments()
            ReportsController().generate_report_tournaments(tournaments)
        elif user_input == "3":
            self.view.report_tournament()
            try:
                ReportsController().generate_report_tournament(self.tournament)
            except Exception:
                self.view.miss_loaded()
                time.sleep(2)
                self.report_menu()
        elif user_input == "4":
            self.view.report_tournament_players()
            try:
                ReportsController().generate_report_players(
                    self.tournament['players_list']
                    )
            except Exception:
                self.view.miss_loaded()
                time.sleep(2)
                self.report_menu()
        elif user_input == "5":
            self.view.report_rounds_tournament()
            try:
                ReportsController().generate_report_rounds_tournament(
                    self.tournament['round_list']
                )
            except Exception:
                self.view.miss_loaded()
                time.sleep(2)
                self.report_menu()
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
        try:
            print(f"\nCurrent Tournament Name: {self.tournament['name']}")
            if len(self.tournament['players_list']) < 1:
                print("=> Please add players to the tournament - Press [2]")
            if self.step_access is False and \
                    len(self.tournament['players_list']) > 0 and \
                    self.tournament['current_round'] < 5:
                print(f"=> Add results of the round \
                    {self.tournament['current_round']} - Press [4]")
            elif self.step_access is True and \
                    len(self.tournament['players_list']) > 0 and \
                    self.tournament['current_round'] < 5:
                print(f"=> Please generate pairs for matchs \
                    (Round {self.tournament['current_round']}) - Press [3]")
        except Exception:
            print("\nCurrent Tournament Name: None")
        db = self.database

        self.view.prompt_for_command_menu()
        user_input = input()
        self.view.terminal_clearing()

        if user_input == "1":
            self.tournament = TournamentController(db).new()
        elif user_input == "2":
            self.tournament['players_list'] = PlayerController(db).add_player()
        elif user_input == "3" and \
                self.tournament['current_round'] < 5 and \
                self.step_access:
            self.tournament['round_list'].append(RoundController(db).generate(
                self.tournament['current_round'],
                self.tournament['players_list']
            ))
            self.step_access = False
        elif user_input == "4" and \
                self.tournament['current_round'] < 5 and \
                not self.step_access:
            self.tournament['round_list'] = MatchController(db).add_result(
                self.tournament['round_list'],
                self.tournament['current_round'] - 1
            )
            self.tournament['players_list'] = RoundController.update_score(
                self.tournament,
                self.tournament['current_round']
            )
            self.tournament['current_round'] = RoundController.update_round(
                self.tournament['current_round']
            )
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
