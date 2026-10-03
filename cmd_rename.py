from game_shelf import GameNotFoundError, GameShelf


def cmd_rename(shelf: GameShelf, *args: str) -> None:
    if len(args) < 2:
        print("Usage: rename id new_title")
        return

    # Convert id from string to int
    try:
        game_id = int(args[0])
    except ValueError:
        print("Error: invalid id value")
        return

    # Handle compound game titles
    new_title = " ".join(args[1:])

    try:
        old_title = shelf.get_game(game_id).title
        updated = shelf.rename_game(game_id, new_title)
        print(f"Game '{old_title}' renamed to '{updated.title}'")
    except GameNotFoundError as e:
        print(f"Error: {e}")
