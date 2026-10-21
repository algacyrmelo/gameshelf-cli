import unittest

from game_shelf import Game, GameNotFoundError, GameShelf, GameStatus
from shelf_conversion import ShelfData, shelf_from_dict, shelf_to_dict


class TestShelfConversion(unittest.TestCase):
    def setUp(self) -> None:
        self.shelf = GameShelf(
            [
                Game(1, "Celeste", GameStatus.PLAYING),
                Game(3, "A Mortician's Tale", GameStatus.BEATEN),
                Game(4, "Valorant", GameStatus.ENDLESS),
            ],
            7,
        )
        self.shelf_data: ShelfData = {
            "next_id": 7,
            "games": [
                {"id": 1, "title": "Celeste", "status": "playing"},
                {"id": 3, "title": "A Mortician's Tale", "status": "beaten"},
                {"id": 4, "title": "Valorant", "status": "endless"},
            ],
        }

    def test_shelf_to_dict(self) -> None:
        shelf_data = shelf_to_dict(self.shelf)
        self.assertEqual(shelf_data, self.shelf_data)

    def test_shelf_from_dict(self) -> None:
        shelf = shelf_from_dict(self.shelf_data)
        self.assertEqual(shelf.list_games(), self.shelf.list_games())
        self.assertEqual(shelf.next_id, self.shelf.next_id)
