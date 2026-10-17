import unittest

from game_shelf import GameNotFoundError, GameShelf, GameStatus


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

    # list_games
    def test_list_games_many(self):
        new_game = self.gameshelf.add_game("Celeste")
        another_game = self.gameshelf.add_game("A Mortician's Tale")
        games = self.gameshelf.list_games()
        self.assertEqual(games, [new_game, another_game])

    def test_list_games_empty(self):
        games = self.gameshelf.list_games()
        self.assertEqual(games, [])

    # rename_game
    def test_rename_game(self):
        game_with_typo = self.gameshelf.add_game("Title with typo")
        game_after = self.gameshelf.rename_game(game_with_typo.id, "Celeste")
        self.assertEqual(game_after.title, "Celeste")

    def test_rename_game_not_found(self):
        self.assertRaises(GameNotFoundError, self.gameshelf.rename_game, 1, "Celeste")

    # get_game
    def test_get_game(self):
        expected = self.gameshelf.add_game("The Legend of Zelda")
        got = self.gameshelf.get_game(expected.id)
        self.assertEqual(expected, got)

    def test_get_game_not_found(self):
        self.assertRaises(GameNotFoundError, self.gameshelf.get_game, 1)


if __name__ == "__main__":
    unittest.main()
