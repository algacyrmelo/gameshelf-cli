import unittest

from game_shelf import Game, GameNotFoundError, GameShelf, GameStatus
from shelf_conversion import GameDict, ShelfDict, shelf_from_dict, shelf_to_dict


class TestShelfConversion(unittest.TestCase):
    def setUp(self) -> None:
        games = [
            Game(1, "Celeste", GameStatus.PLAYING),
            Game(3, "A Mortician's Tale", GameStatus.BEATEN),
            Game(4, "Valorant", GameStatus.ENDLESS),
        ]
        game_dicts: list[GameDict] = [
            {"id": 1, "title": "Celeste", "status": "playing"},
            {"id": 3, "title": "A Mortician's Tale", "status": "beaten"},
            {"id": 4, "title": "Valorant", "status": "endless"},
        ]
        self.shelf = GameShelf(games, next_id=7)
        self.shelf_dict: ShelfDict = {"next_id": 7, "games": game_dicts}

    def test_shelf_to_dict(self) -> None:
        result = shelf_to_dict(self.shelf)
        self.assertEqual(result, self.shelf_dict)

    def test_shelf_to_dict_empty(self) -> None:
        result = shelf_to_dict(GameShelf())
        self.assertEqual(result, {"next_id": 1, "games": []})

    def test_shelf_from_dict(self) -> None:
        result = shelf_from_dict(self.shelf_dict)
        self.assertEqual(result.list_games(), self.shelf.list_games())
        self.assertEqual(result.next_id, self.shelf.next_id)

    def test_shelf_from_dict_empty(self) -> None:
        result = shelf_from_dict({"next_id": 1, "games": []})
        self.assertEqual(result.list_games(), [])
        self.assertEqual(result.next_id, 1)

    def test_shelf_round_trip(self) -> None:
        result = shelf_from_dict(shelf_to_dict(self.shelf))
        self.assertEqual(result.list_games(), self.shelf.list_games())
        self.assertEqual(result.next_id, self.shelf.next_id)
