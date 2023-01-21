"""Report Views."""

from views.menu_views import MenuViews


class ReportViews(MenuViews):
    """Implement the view."""

    def run_report():
        ReportViews.app_title()
        ReportViews.terminal_clearing()
        ReportViews.app_title()
        ReportViews.report_title()
        ReportViews.report_list()

    def report_title():
        print("# REPORT\n")

    def report_list():
        """Show the Report list."""
        print("[1] - List players by alphabetical order.")
        print("[2] - List all tournaments.")
        print("[3] - List the tournament name with date of the event.")
        print("[4] - List players tournament by alphabetical order.")
        print("[5] - list all rounds of the tournament.")
        print("[8] - Return to the menu.")
        print("[9] - Quit the App.")
        print("\n")

    def report_players():
        """Show players title section."""
        print("----------------------------------------")
        print("List players by alphabetical order: ")
        print("----------------------------------------\n")

    def report_tournaments():
        """Show all tournaments title section."""
        print("----------------------------------------")
        print("List tournaments: ")
        print("----------------------------------------\n")

    def report_tournament():
        """Show the tournament title section."""
        print("----------------------------------------")
        print("List a tournament: ")
        print("----------------------------------------\n")

    def report_tournament_players():
        """Show the tournament players title section."""
        print("----------------------------------------")
        print("List tournament players by alphabetical order: ")
        print("----------------------------------------\n")

    def report_rounds_tournament():
        """Show the add player title section."""
        print("----------------------------------------")
        print("List all rounds tournament: ")
        print("----------------------------------------\n")
