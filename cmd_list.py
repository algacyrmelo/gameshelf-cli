def cmd_list(shelf, *args):
    games = shelf.list_games()
    if len(games) == 0:
        print("The shelf is empty")
        return

    for id, title, status in games:
        print(f"[{id}] {title} ({status})")
