import sys

from game_shelf import Shelf


def cmd_exit(shelf: Shelf, *args: str) -> None:
    print("Exiting...")
    sys.exit()
