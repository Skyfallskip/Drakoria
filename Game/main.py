import arcade as arc
from Game.Core.Views import GameView
from Game.Core.Views import screen_width, screen_height, screen_title

def main():
    """ Main function """

    window = arc.Window(screen_width, screen_height, screen_title)


    game = GameView()
    game.setup()


    window.show_view(game)


    arc.run()


if __name__ == "__main__":
    main()