class GameNotFoundError(Exception): ...


class GameShelf:
    def __init__(self) -> None:
        self.games = []
        self.next_id = 1

    def add_game(self, title: str) -> None:
        self.games.append({"id": self.next_id, "title": title, "status": "playing"})
        self.next_id += 1

    def list_games(self) -> list[tuple]:
        return [(game["id"], game["title"], game["status"]) for game in self.games]

    def rename_game(self, id: int, new_title: str) -> tuple[str, str]:
        for i, game in enumerate(self.games):
            if game["id"] == id:
                old_title = game["title"]
                self.games[i]["title"] = new_title
                return (old_title, new_title)

        raise GameNotFoundError(f"Game with id {id} not found")
