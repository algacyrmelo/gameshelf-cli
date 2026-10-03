import sys

from game_shelf import GameShelf


def cmd_exit(shelf: GameShelf, *args: str) -> None:
    print("Exiting...")
    sys.exit()
