from typing import TypedDict

from game_shelf import Game, GameShelf, GameStatus


class GameData(TypedDict):
    id: int
    title: str
    status: str


class ShelfData(TypedDict):
    next_id: int
    games: list[GameData]


def shelf_to_dict(shelf: GameShelf) -> ShelfData:
    games: list[GameData] = []

    # TODO: Create game_to_dict
    for game in shelf.list_games():
        game_data: GameData = {
            "id": game.id,
            "title": game.title,
            "status": game.status.value,
        }
        games.append(game_data)

    return {"next_id": shelf.next_id, "games": games}


def shelf_from_dict(shelf_data: ShelfData) -> GameShelf:
    games: list[Game] = []
    for game_data in shelf_data["games"]:
        game = Game(
            game_data["id"], game_data["title"], GameStatus(game_data["status"])
        )
        games.append(game)
    return GameShelf(games, shelf_data["next_id"])
