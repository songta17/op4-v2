"""Match Views."""
CURRENT_MATCH = {
    0: 'first',
    1: 'second',
    2: 'third',
    3: 'fourth'
}


class MatchViews:
    """Implement the Round views."""

    def match_title(number):
        """Show Match title section."""
        print("--------------------------------------")
        print(f"Add the result for the {CURRENT_MATCH[int(number)]} match:")
        print("--------------------------------------\n")

    def add_result_match(player_one, player_two):
        txt = f"PLAYER ONE [{player_one}] VS " \
            f"PLAYER TWO [{player_two}]\n"
        print(txt)
        hint_result = "PLAYER ONE WIN press [1] | " \
            "PLAYER TWO WIN press [2] | " \
            "DRAW press any key"
        print(hint_result)
        print("> ", end="")
        return input()
