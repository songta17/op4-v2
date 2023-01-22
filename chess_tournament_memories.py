"""Entry point."""

from controllers.menu_controller import MenuController


class App:
    def __init__(self):
        game = MenuController()
        game.main_menu()


if __name__ == "__main__":
    """Launch of the chess memory tournament app."""
    App()
