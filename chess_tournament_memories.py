"""Entry point."""

from controllers.game_controller import GameController


class App:
    def __init__(self):
        game = GameController()
        game.main_menu()

if __name__ == "__main__":
    """Launch of the chess memory tournament app."""
    App()