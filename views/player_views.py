"""Player Views."""


class PlayerViews:
    """Implement the Player views."""

    def add_player_title_section():
        """Show the Add Player title section."""
        print("----------------------------------------")
        print("Please Add Player for the tournament: ")
        print("----------------------------------------\n")

    def prompt_national_id():
        """Ask for the national_id of a player."""
        print("\nPlease type the player national id: ")
        print(">", end="")
        return input()

    def prompt_lastname():
        """Ask for the lastname of a player."""
        print("\nPlease type the player lastname: ")
        print(">", end="")
        return input()

    def prompt_firstname():
        """Ask for the firstname of a player."""
        print("\nPlease type the player firstname: ")
        print(">", end="")
        return input()

    def prompt_dob():
        """Ask for the date of birth of a player."""
        print("\nPlease type the player date of birth: ")
        print(">", end="")
        return input()

    def player_added_msg(player_number):
        """Adding player message."""
        print(f"\nThe player {player_number} was added.")
        print(">", end="")

    def error_add_player():
        """Error message to the menu."""
        print("\nAn error occured during the adding of a player.")
