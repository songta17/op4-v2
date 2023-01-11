"""Define tournament."""
# from player import Player


class Tournament:
    """Tournament class."""

    def __init__(
            self,
            name,
            place,
            start_date,
            end_date,
            round_list=[],
            players_list=[],
            current_round=1,
            round_number=4,
            description=None
            ):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.current_round = current_round
        self.round_list = round_list
        self.players_list = players_list
        self.round_number = round_number
        self.description = description

    def __repr__(self, *args, **kwargs):
        return str(vars(self))

    def add_player(self, new_player):
        self.players_list.append(new_player)

    def add_round(self, new_round):
        self.players_list.append(new_round)

    def edit_description(self, new_description):
        self.description = new_description

    def sort_players_by_name(self):
        # self.players_list.sorted(self.players_list.items(), key="lastname")
        # sorted(self.players_list, key=lambda i: i['lastname'])
        pass

    def serialize_tournament(self):
        return {
            'name': self.name,
            'place': self.place,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'current_round': self.current_round,
            'round_list': self.round_list,
            'players_list': self.players_list,
            'round_number': self.round_number,
            'description': self.description
        }

    # def sort_players_by_score(self, array):
        # return sorted(array, key=lambda i: i['name'])

    # def save_tournament(self):
    #     pass

    # def load_tournament(self):
    #     pass

# players = []
# player = Player(
#     "AB01",
#     "Phou",
#     "Vora",
#     "14/01/79"
# )
# player2 = Player(
#     "AB02",
#     "Nor",
#     "Sith",
#     "01/12/79"
# )
# players.append(player)
# players.append(player2)

# tournament = Tournament(
#     "name tournament",
#     "Marly",
#     "01/01/2023",
#     "10/01/2023",
#     1,
#     ["round list"],
#     players,
#     "time control",
#     4,
#     "sans description"
# )
# # tournament = Tournament(
# #     "name tournament",
# #     "Marly",
# #     "01/01/2023",
# #     "10/01/2023",
# #     1,
# #     ["round list"],
# #     ["z", "a", "player one", "player two"],
# #     "time control",
# #     4,
# #     "sans description"
# # )
# print(tournament)
# print("---------------")
# tournament.add_player("John")
# # print(tournament.sort_players_by_name())
# # print(sort_players_by_name(tournament.players_list))
# # print(str(tournament))
# # tournament.sort_players_by_score()
# print("---------------")
# # tournament.sort_players_by_name()
# # print(str(tournament))
# # tournament.edit_description("hello description!")
# # print(str(tournament))
