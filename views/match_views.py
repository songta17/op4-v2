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
        print(f"Add the result for the {CURRENT_MATCH[int(number)]} match below: ")
        print("--------------------------------------\n")

    def add_result_match(player_one, player_two):
        print(f"\033[92mPLAYER ONE [{player_one}]\033[0m VS \033[92mPLAYER TWO [{player_two}]\033[0m\n")
        print("PLAYER ONE WIN press [1] | PLAYER TWO WIN press [2] | DRAW press any key")
        print("> ", end="")
        return input()