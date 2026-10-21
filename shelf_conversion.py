from typing import TypedDict

from game_shelf import Game, GameShelf, GameStatus


class GameDict(TypedDict):
    id: int
    title: str
    status: str


class ShelfDict(TypedDict):
    next_id: int
    games: list[GameDict]


def game_to_dict(game: Game) -> GameDict:
    return {"id": game.id, "title": game.title, "status": game.status.value}


def game_from_dict(game: GameDict) -> Game:
    return Game(game["id"], game["title"], GameStatus(game["status"]))


def shelf_to_dict(shelf: GameShelf) -> ShelfDict:

    games: list[GameDict] = []
    for game in shelf.list_games():
        games.append(game_to_dict(game))

    return {"next_id": shelf.next_id, "games": games}


def shelf_from_dict(shelf: ShelfDict) -> GameShelf:

    games: list[Game] = []
    for game_dict in shelf["games"]:
        games.append(game_from_dict(game_dict))

    return GameShelf(games, shelf["next_id"])
