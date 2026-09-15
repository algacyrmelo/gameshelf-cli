from game_shelf import GameNotFoundError


def cmd_rename(shelf, *args):
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
        old_title, new_title = shelf.rename_game(game_id, new_title)
        print(f"Game {old_title} renamed to {new_title}")
    except GameNotFoundError as e:
        print(f"Error: {e}")
