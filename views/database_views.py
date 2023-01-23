"""Database Views."""


class DatabaseViews:
    """Implement the view."""

    def database_title_section():
        """Show the database title section."""
        print("--------------------------------------")
        print("Database: ")
        print("--------------------------------------\n")

    def saving_tournament():
        """Tournament is saving."""
        print("The tournament is saving. Pleae wait.")

    def loading_tournament():
        """Tournament is loading."""
        print("The tournament is loading. Pleae wait.")

    def tournament_list_ids():
        print("---------------------------")
        print("--- Tournament List Ids ---")
        print("---------------------------")
        print("ID - Tournament name")

    def show_id_printer(id, name):
        print(f"{int(id)} - {name}")

    def show_tournaments_ids(tournaments):
        print("id disponible:")
        print(len(tournaments))
        print("\n")

    def load_number_id():
        """Ask number id."""
        print("\nPlease add the tournament id for loading the tournament.")
        print("> ", end="")
        return input()
