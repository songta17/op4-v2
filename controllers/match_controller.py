"""Define the match controller."""
import json
from datetime import date

from views.match_views import MatchViews
from views.menu_views import MenuViews

APPLY_POINT = {'win': 1, 'lose': 0, 'draw': 0.5}


class MatchController:
    """Match controller."""

    def __init__(self, database):
        self.database = database

    def add_result(self, round_list, current_round):
        matchs = round_list[current_round]['matchs_list']

        for i in range(4):
            MatchViews.match_title(i)
            result = MatchViews.add_result_match(
                matchs[i]['player_1_name'],
                matchs[i]['player_2_name']
            )

            if result == "1":
                matchs[i]['score_player_1'] = APPLY_POINT["win"]
                matchs[i]['score_player_2'] = APPLY_POINT["lose"]
            elif result == "2":
                matchs[i]['score_player_1'] = APPLY_POINT["lose"]
                matchs[i]['score_player_2'] = APPLY_POINT["win"]
            else:
                matchs[i]['score_player_1'] = APPLY_POINT["draw"]
                matchs[i]['score_player_2'] = APPLY_POINT["draw"]
            MenuViews.terminal_clearing()

        end_start = date.today()
        round_list[current_round]['end_time'] = json.dumps(
            end_start,
            default=str
            )
        return round_list
