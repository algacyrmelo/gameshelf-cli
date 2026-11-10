import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from persistence import load, save
from shelf import Game, GameStatus, Shelf


class TestPersistence(unittest.TestCase):
    def setUp(self) -> None:
        self.games = [
            Game(1, "Celeste", GameStatus.PLAYING),
            Game(3, "A Mortician's Tale", GameStatus.BEATEN),
            Game(4, "Valorant", GameStatus.ENDLESS),
        ]

    def test_save_and_load_roundtrip(self):
        s = Shelf(self.games, 7)
        with TemporaryDirectory() as tmpdir:
            fp = Path(tmpdir) / "teste.json"

            save(s, fp)
            result = load(fp)

            self.assertEqual(result.list_games(), s.list_games())
            self.assertEqual(result.next_id, 7)

    def test_load_first_time(self):
        with TemporaryDirectory() as tmpdir:
            fp = Path(tmpdir) / "teste.json"

            result = load(fp)

            self.assertEqual(result.list_games(), [])
            self.assertEqual(result.next_id, 1)


if __name__ == "__main__":
    unittest.main()
