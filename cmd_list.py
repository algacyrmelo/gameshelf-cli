from game_shelf import Shelf


def cmd_list(shelf: Shelf, *args: str) -> None:
    games = shelf.list_games()
    if len(games) == 0:
        print("The shelf is empty")
        return

    for game in games:
        print(f"[{game.id}] {game.title} ({game.status.value})")
