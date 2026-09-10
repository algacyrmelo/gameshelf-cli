import sys


def cmd_add(shelf, *args):
    title = input("Enter the game title: ")
    shelf.add_game(title)


def cmd_list(shelf, *args):
    shelf.list_games()


def cmd_help(shelf, *args):
    print()
    print("GameShelf CLI")
    print("Usage:")
    print()
    commands = get_commands()
    for name, cmd in commands.items():
        print(f"- {name}: {cmd['desc']}")
    print()


def cmd_exit(shelf, *args):
    print("Exiting GameShelf CLI...")
    sys.exit()


def get_commands():
    return {
        "add": {"desc": "Add a new game", "callback": cmd_add},
        "list": {"desc": "List games", "callback": cmd_list},
        "help": {"desc": "Show command options", "callback": cmd_help},
        "exit": {"desc": "Exit gameshelf", "callback": cmd_exit},
    }
