from command_registry import get_commands
from game_shelf import GameShelf


def split_input(text: str) -> list[str]:
    words = text.split()
    return words


def main():
    shelf = GameShelf()

    commands = get_commands()
    while True:
        words = split_input(input("gameshelf > "))
        if len(words) == 0:
            continue
        command_name = words[0]

        args = []
        if len(words) > 1:
            args = words[1:]

        command = commands.get(command_name)
        if not command:
            print("Unknown command")
            continue

        command["callback"](shelf, *args)


if __name__ == "__main__":
    main()
