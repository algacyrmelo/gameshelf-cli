from shelf import Game, GameStatus, Shelf
from typed import GameDict, ShelfDict


def game_to_dict(game: Game) -> GameDict:
    return {"id": game.id, "title": game.title, "status": game.status.value}


def game_from_dict(game: GameDict) -> Game:
    return Game(game["id"], game["title"], GameStatus(game["status"]))


def shelf_to_dict(shelf: Shelf) -> ShelfDict:

    games: list[GameDict] = []
    for game in shelf.list_games():
        games.append(game_to_dict(game))

    return {"next_id": shelf.next_id, "games": games}


def shelf_from_dict(shelf: ShelfDict) -> Shelf:

    games: list[Game] = []
    for game_dict in shelf["games"]:
        games.append(game_from_dict(game_dict))

    return Shelf(games, shelf["next_id"])
