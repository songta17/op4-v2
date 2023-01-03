"""Define round."""


class Round:
    """Round model."""

    def __init__(self, round_number, matchs_list):
        self.round_number = round_number
        self.matchs_list = matchs_list

    def __repr__(self):
        return str(vars(self))

# instance_match_1 = [('john', 'sarah'), ('michel', 'augustin'), ('Maxhildan', 'Zouloux')]
# round = Round(1, instance_match_1)
# print(round)