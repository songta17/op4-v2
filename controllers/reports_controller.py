"""Define the reports controller."""
from prettytable import PrettyTable


class ReportsController:
    """Reports controller."""

    def __init__(self):
        self.report = PrettyTable()

    # MENU REPORT [2]
    def report_tournaments(self, tournaments):
        """Generate all tournaments name."""
        breakpoint()

    # MENU REPORT [3]
    def report_tournament(self, tournament):
        """Generate the report of the tournament loaded."""
        self.report.field_names = [
            "Tournament Name",
            "Start Date",
            "End Date"
        ]

        self.report.add_row([
                tournament['name'],
                tournament['start_date'],
                tournament['end_date']
            ])
        print(self.report)

    # MENU REPORT [4]
    def report_players(self, players):
        """Generate the report of all players of the tournament loaded."""
        self.report.field_names = [
            "ID",
            "National Id",
            "Lastname",
            "Firstname",
            "Date of Birth",
            "Score"
        ]

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
        
        print(self.report)

    # MENU REPORT [5]
    def report_rounds_tournament(self, rounds_list):
        """Generate the report of all rounds of the tournament loaded."""
        self.report.field_names = [
            "round_name",
            "matchs_list",
            "start_time",
            "end_time"
        ]

        for i in range(len(rounds_list)): 
            self.report.add_row(["", "", "", ""])
            self.report.add_row([    
                    rounds_list[i]['round_name'],
                    " [Player 1][point] VS [Player 2][point]" ,
                    rounds_list[i]['start_time'],
                    rounds_list[i]['end_time']
                ])

            for y in range(4):
                p1 = rounds_list[i]['matchs_list'][int(y)]['player_1_name']
                s1 = rounds_list[i]['matchs_list'][int(y)]['score_player_1']
                p2 = rounds_list[i]['matchs_list'][int(y)]['player_2_name']
                s2 = rounds_list[i]['matchs_list'][int(y)]['score_player_2']
                
                self.report.add_row([
                    "", 
                    p1 + "(" + str(s1) + ")" + " VS " + p2 + "(" + str(s2) + ")", 
                    "", 
                    ""
                ])
            
        round = self.report

        print(round)
