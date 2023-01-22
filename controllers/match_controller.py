"""Define the match controller."""
import json
from datetime import datetime


class MatchController:
    """Match controller."""

    def __init__(self, database):
        self.database = database

    def add_result(self, round_list, current_round):
        for i in range(4):
            reduce = round_list[current_round]['matchs_list']
            print(f"match: {reduce[i]['player_1_name']} vs {reduce[i]['player_2_name']}")
            result = input()

            if result == "1":
                reduce[i]['score_player_1'] = 1
                reduce[i]['score_player_2'] = 0
            elif result == "2":
                reduce[i]['score_player_1'] = 0
                reduce[i]['score_player_2'] = 1
            else:
                reduce[i]['score_player_1'] = 0.5
                reduce[i]['score_player_2'] = 0.5

        end_start = datetime.now()
        round_list[current_round]['end_time'] = json.dumps(end_start, default=str)
        # self.database.table_tournaments.update({'round_list': round_list})
        return round_list
