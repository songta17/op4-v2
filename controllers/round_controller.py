"""Define the round controller."""
import time
import pprint
from datetime import datetime

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
        start_time = datetime.now()
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

        # self.database.table_tournaments.update(
        #     {'round_list': round.serialize_round()}
        # )
        return round.serialize_round()

    def update_round(current_round):
        return current_round + 1

    def ranking(players):
        # trier les joueurs en fonction de leur
        # resultats dans le tournoi en cours
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
            score = tournament['players_list'][i]['score']

            for n in range(4):
                # breakpoint()
                if tournament['round_list'][current - 1]['matchs_list'][int(n)]['player_1'] == player_national_id:
                    score = score + tournament['round_list'][current - 1]['matchs_list'][int(n)]['score_player_1']
                    break
                if tournament['round_list'][current - 1]['matchs_list'][int(n)]['player_2'] == player_national_id:
                    score = score + tournament['round_list'][current - 1]['matchs_list'][int(n)]['score_player_2']
                    break
            print(f"new_score: {score} -------")
            tournament['players_list'][i]['score'] = score
        return tournament['players_list']



    def players_rank_order(sorted_players):
        """Get all national_id during a round."""
        national_id_ranks = []
        for index in range(len(sorted_players)):
            national_id_ranks.append(sorted_players[index]['national_id'])
        return national_id_ranks

    def generate_pair(sorted_players):
        # create a natina_id list ranked for the round 
        national_id_ranks = RoundController.players_rank_order(sorted_players)   
        national_id_ranks.reverse()     
        array = []
        i = 0

        while i < 4:
            for xx in range(8):
                if not national_id_ranks[(xx)] in sorted_players[i]['opponents'] and sorted_players[i]['national_id'] != national_id_ranks[(xx)]:
                    oppenent = national_id_ranks.pop(xx)
                    sorted_players[i]['opponents'].append(oppenent)
                    for xxx in range(8):
                        if oppenent == sorted_players[xxx]['national_id']:
                            sorted_players[xxx]['opponents'].append(sorted_players[i]['national_id'])
                            break
                    break

            match = Match(
                sorted_players[i]['national_id'],
                sorted_players[i]['firstname'] + " " + sorted_players[i]['lastname'],
                sorted_players[xxx]['national_id'],
                sorted_players[xxx]['firstname'] + " " + sorted_players[xxx]['lastname']
            )
            array.append(match.serialize_match())
            i += 1

        return array
