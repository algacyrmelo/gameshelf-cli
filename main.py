from commands import get_commands
from game_shelf import GameShelf


def main():
    shelf = GameShelf()

    commands = get_commands()
    while True:
        print()

        # TODO: Normalize user input
        # TODO: Split user input between command and optional arguments
        command_name = input("gameshelf > ")

        command = commands.get(command_name)
        if not command:
            print("You've entered an invalid command")
            continue

        command["callback"](shelf)


if __name__ == "__main__":
    main()
