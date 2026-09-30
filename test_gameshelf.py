import unittest

from game_shelf import GameShelf


class TestGameShelf(unittest.TestCase):
    def setUp(self) -> None:
        self.gameshelf = GameShelf()

    def test_add_game(self):
        self.gameshelf.add_game("Celeste")

        games = self.gameshelf.list_games()
        self.assertEqual(len(games), 1)

        game_id, game_title, game_status = games[0]
        self.assertEqual(game_id, 1)
        self.assertEqual(game_title, "Celeste")
        self.assertEqual(game_status, "playing")

    def test_add_game_unique_id(self):
        self.gameshelf.add_game("Celeste")
        self.gameshelf.add_game("Resident Evil 4")

        games = self.gameshelf.list_games()

        game1_id = games[0][0]
        game2_id = games[1][0]
        self.assertNotEqual(game1_id, game2_id)


if __name__ == "__main__":
    unittest.main()
