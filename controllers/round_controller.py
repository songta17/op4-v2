"""Define the round controller."""
import time
from datetime import date

from models.round import Round
from models.match import Match
from views.round_views import RoundViews
from views.menu_views import MenuViews


class RoundController:
    """Player controller."""

    def __init__(self, database):
        self.view = RoundViews
        self.database = database
        self.round_list = []

    def generate(self, current_round, players):
        """Add players."""
        self.view.generate_pairs_title_section(current_round)
        round_name = "Round " + str(current_round)
        matchs_list = []
        start_time = date.today()
        sorted_players = RoundController.ranking(players)
        matchs_list = RoundController.generate_pair(sorted_players)

        try:
            round = Round(
                round_name,
                matchs_list,
                start_time
            )
            time.sleep(3)
            MenuViews.redirect_to_menu_msg()
        except Exception:
            print("error save round")
            time.sleep(3)
            MenuViews.redirect_to_menu_msg()
        return round.serialize_round()

    def update_round(current_round):
        return current_round + 1

    def ranking(players):
        return sorted(
            players,
            key=lambda player: player['score'],
            reverse=True
        )

    def update_score(tournament, current):
        """update score"""
        for i in range(8):
            """Joueur """
            print(f'------ PLAYER {i+1} -------')
            player_national_id = tournament['players_list'][i]['national_id']
            old_score = tournament['players_list'][i]['score']
            round_list = tournament['round_list'][current - 1]

            for n in range(4):
                match_player = round_list['matchs_list'][int(n)]
                point_p1 = match_player['score_player_1']
                point_p2 = match_player['score_player_2']
                if match_player['player_1'] == player_national_id:
                    new_score = old_score + point_p1
                    break
                if match_player['player_2'] == player_national_id:
                    new_score = old_score + point_p2
                    break
            old_score = new_score
            tournament['players_list'][i]['score'] = new_score
        return tournament['players_list']

    def players_rank_order(sorted_players):
        """Get all national_id during a round."""
        national_id_ranks = []
        for index in range(len(sorted_players)):
            national_id_ranks.append(sorted_players[index]['national_id'])
        return national_id_ranks

    def generate_pair(players):
        """create a natina_id list ranked for the round."""
        national_id_ranks = RoundController.players_rank_order(players)
        national_id_ranks.reverse()
        array = []
        i = 0

        while i < 4:
            for y in range(8):
                if not national_id_ranks[(y)] in players[i]['opponents'] and \
                        players[i]['national_id'] != national_id_ranks[(y)]:
                    oppenent = national_id_ranks.pop(y)
                    players[i]['opponents'].append(oppenent)
                    for n in range(8):
                        players[n]['national_id']
                        if oppenent == players[n]['national_id']:
                            players[n]['opponents'].append(
                                players[i]['national_id']
                                )
                            break
                    break

            match = Match(
                players[i]['national_id'],
                players[i]['firstname'] + " " + players[i]['lastname'],
                players[n]['national_id'],
                players[n]['firstname'] + " " + players[n]['lastname']
            )
            array.append(match.serialize_match())
            i += 1

        return array
