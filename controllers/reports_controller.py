"""Define the reports controller."""

from prettytable import PrettyTable
from views.report_views import ReportViews


class ReportsController:
    """Reports controller."""
    def __init__(self):
        self.report = PrettyTable()
        self.views = ReportViews

    # MENU REPORT [1]
    def create_players_tournaments_table(self):
        """Generate the table of all players tournaments."""
        self.report.field_names = [
            "National Id",
            "Lastname",
            "Firstname",
            "Date of Birth"
        ]

    def add_players_tournaments_content(self, players):
        """Add data to the table of all players tournaments."""
        players_order_by_name = sorted(
            players,
            key=lambda player: player['lastname'],
            reverse=False
        )

        for i in range(len(players)):
            self.report.add_row([
                players_order_by_name[i]['national_id'],
                players_order_by_name[i]['lastname'],
                players_order_by_name[i]['firstname'],
                players_order_by_name[i]['dob']
            ])

    def report_players_tournaments(self, players):
        """Generate players name of all tournaments."""
        self.create_players_tournaments_table()
        self.add_players_tournaments_content(players)
        print(self.report)

    # MENU REPORT [2]
    def create_tournaments_table(self):
        """Create the table for the report tournaments."""
        self.report.field_names = [
            "ID",
            "Tournament Name",
            "Start Date",
            "End Date"
        ]

    def add_tournaments_content(self, tournaments):
        """Add the data for the report tournaments."""
        for i in range(len(tournaments)):
            self.report.add_row([
                    i,
                    tournaments[int(i)]['name'],
                    tournaments[int(i)]['start_date'],
                    tournaments[int(i)]['end_date']
                ])

    def generate_report_tournaments(self, tournaments):
        """Generate all tournaments name report."""
        self.create_tournaments_table()
        self.add_tournaments_content(tournaments)
        print(self.report)

    # MENU REPORT [3]
    def create_tournament_table(self):
        """Create the table for a tournament report."""
        self.report.field_names = [
            "Tournament Name",
            "Start Date",
            "End Date"
        ]

    def add_tournament_content(self, tournament):
        """Add the data for a tournament report."""
        self.report.add_row([
                tournament['name'],
                tournament['start_date'],
                tournament['end_date']
            ])

    def generate_report_tournament(self, tournament):
        """Generate the tournament report."""
        self.create_tournament_table()
        self.add_tournament_content(tournament)
        print(self.report)

    # MENU REPORT [4]
    def create_players(self):
        """Create the table for the players report."""
        self.report.field_names = [
            "ID",
            "National Id",
            "Lastname",
            "Firstname",
            "Date of Birth",
            "Score"
        ]

    def add_players_content(self, players):
        """Add the data for the players report."""
        players_order_by_name = sorted(
            players,
            key=lambda player: player['lastname'],
            reverse=False
        )

        for i in range(8):
            self.report.add_row([
                i,
                players_order_by_name[i]['national_id'],
                players_order_by_name[i]['lastname'],
                players_order_by_name[i]['firstname'],
                players_order_by_name[i]['dob'],
                players_order_by_name[i]['score']
            ])

    def generate_report_players(self, players):
        """Generate the report of all players of the tournament loaded."""
        self.create_players()
        self.add_players_content(players)
        print(self.report)

    # MENU REPORT [5]
    def create_rounds_tournament(self):
        """Create the tabble for reports players."""
        self.report.field_names = [
            "round_name",
            "matchs_list",
            "start_time",
            "end_time"
        ]

    def add_rounds_tournament(self, rounds_list):
        """Add the table for reports players."""
        for i in range(len(rounds_list)):
            self.report.add_row(["", "", "", ""])
            self.report.add_row([
                    rounds_list[i]['round_name'],
                    " [Player 1][point] VS [Player 2][point]",
                    rounds_list[i]['start_time'],
                    rounds_list[i]['end_time']
                ])

            for y in range(4):
                p1 = rounds_list[i]['matchs_list'][int(y)]['player_1_name']
                s1 = rounds_list[i]['matchs_list'][int(y)]['score_player_1']
                p2 = rounds_list[i]['matchs_list'][int(y)]['player_2_name']
                s2 = rounds_list[i]['matchs_list'][int(y)]['score_player_2']
                versus_opponents = self.views.show_opponents(p1, s1, p2, s2)

                self.report.add_row([
                    "",
                    versus_opponents,
                    "",
                    ""
                ])

    def generate_report_rounds_tournament(self, rounds_list):
        """Generate the report of all rounds of the tournament loaded."""
        self.create_rounds_tournament()
        self.add_rounds_tournament(rounds_list)
        print(self.report)
