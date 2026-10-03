from game_shelf import GameShelf


def cmd_add(shelf: GameShelf, *args: str) -> None:
    if len(args) == 0:
        print("Usage: add new_title")
        return

    game_title = " ".join(args)
    game = shelf.add_game(game_title)
    print(f"New game added: '{game.title}'")
