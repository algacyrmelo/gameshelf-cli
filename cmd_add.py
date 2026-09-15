def cmd_add(shelf, *args):
    if len(args) == 0:
        print("Usage: add new_title")
        return

    game_title = " ".join(args)
    shelf.add_game(game_title)
    print(f"New game added: {game_title}")
