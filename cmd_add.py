from persistence import DATA_FILE, save
from shelf import Shelf


def cmd_add(shelf: Shelf, *args: str) -> None:
    if len(args) == 0:
        print("Usage: add new_title")
        return

    game_title = " ".join(args)
    game = shelf.add_game(game_title)
    print(f"New game added: '{game.title}'")

    save(shelf, DATA_FILE)
