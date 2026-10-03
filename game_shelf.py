from dataclasses import dataclass
from enum import Enum


class GameNotFoundError(Exception): ...


class GameStatus(Enum):
    PLAYING = "playing"
    BEATEN = "beaten"
    PLATINUMED = "platinumed"
    DROPPED = "dropped"
    ENDLESS = "endless"


@dataclass
class Game:
    id: int
    title: str
    status: GameStatus = GameStatus.PLAYING


class GameShelf:
    def __init__(self) -> None:
        self.games = []
        self.next_id = 1

    def add_game(self, title: str) -> Game:
        new_game = Game(self.next_id, title)
        self.games.append(new_game)
        self.next_id += 1
        return new_game

    def list_games(self) -> list[Game]:
        return [game for game in self.games]

    def rename_game(self, game_id: int, new_title: str) -> Game:
        game = self.get_game(game_id)
        game.title = new_title
        return game

    def get_game(self, game_id: int) -> Game:
        for game in self.games:
            if game.id == game_id:
                return game
        raise GameNotFoundError(f"Game with id {game_id} not found")
