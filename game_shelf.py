class GameShelf:
    def __init__(self) -> None:
        self.games = []
        self.next_id = 0

    def add_game(self, title):
        self.games.append({"id": self.next_id, "title": title, "status": "playing"})
        self.next_id += 1

    def list_games(self):
        for game in self.games:
            print(game)
