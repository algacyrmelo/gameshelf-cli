import sys


# TODO: Add a command registry.
# TODO: Separate I/O operations from core logic.
class GameShelf:
    def __init__(self) -> None:
        self.games = []
        self.next_id = 0

    def add_game(self):
        title = input("Enter the game title: ")
        self.games.append({"id": self.next_id, "title": title, "status": "playing"})
        self.next_id += 1

    def list_games(self):
        for game in self.games:
            print(game)

    def show_menu(self):
        print("GameShelf CLI\n")

        print("Command Menu:\n")
        print("- new: Adds a new game")
        print("- list: List all games")
        print("- exit: Exit program")
        print()


def main():
    shelf = GameShelf()
    while True:
        shelf.show_menu()
        command = input("gameshelf> ")

        if command == "exit":
            print("Exiting...")
            sys.exit()

        if command == "new":
            shelf.add_game()
        elif command == "list":
            shelf.list_games()


main()
