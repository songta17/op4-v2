"""Tournament Views."""


class TournamentViews:
    """Implement the view."""

    def new_tournament_title_section():
        """Show the new tournament title section."""
        print("--------------------------------------")
        print("Fill the form to create a tournament: ")
        print("--------------------------------------\n")

    def prompt_tournament_name():
        """Ask for the tournament name."""
        print("Please type the tournament name: ")
        print("> ", end="")
        return input()

    def prompt_tournament_place():
        """Ask for the tournament place."""
        print("\nPlease type the tournament location: ")
        print("> ", end="")
        return input()

    def prompt_tournament_start_date():
        """Ask for the tournament start date."""
        print("\nPlease type the starting date of the tournament: ")
        print("> ", end="")
        return input()

    def prompt_tournament_end_date():
        """Ask for the tournament end date."""
        print("\nPlease type the ending date of the tournament: ")
        print("> ", end="")
        return input()

    def prompt_tournament_round_list():
        """Ask round list."""
        print("\nPlease type the tournament round list.")
        print("> ", end="")
        return input()

    def prompt_tournament_players_list():
        """Ask rank."""
        print("\nPlease add a player.")
        print("> ", end="")
        return input()

    def tournament_created_msg():
        """Tournament created."""
        print("\n\033[92mTournament created!\033[0m")

    def prompt_tournament_time_control():
        """Ask rank."""
        print("\nPlease type the time control [].")
        print("> ", end="")
        return input()

    def error_create_tournament():
        """Error message to the menu."""
        print("\nAn error occured during the creation of the tournament.")

    def add_description():
        """Ask description."""
        print("\nPlease add the description of the tournament.")
        print("> ", end="")
        return input()

    def load_number_id():
        """Ask number id."""
        print("\nPlease add the tournament id for loading the tournament.")
        print("> ", end="")
        return input()
