import unittest

from game_shelf import GameShelf, GameStatus


class TestGameShelf(unittest.TestCase):
    def setUp(self) -> None:
        self.gameshelf = GameShelf()

    # add_game
    def test_add_game(self):
        self.gameshelf.add_game("Celeste")

        games = self.gameshelf.list_games()
        self.assertEqual(len(games), 1)

        game = games[0]
        game_id, title, status = game.id, game.title, game.status
        self.assertEqual(game_id, 1)
        self.assertEqual(title, "Celeste")
        self.assertEqual(status, GameStatus.PLAYING)

    def test_add_game_unique_ids(self):
        self.gameshelf.add_game("Celeste")
        self.gameshelf.add_game("Resident Evil 4")

        games = self.gameshelf.list_games()
        first = games[0]
        second = games[1]
        self.assertNotEqual(first.id, second.id)


if __name__ == "__main__":
    unittest.main()
