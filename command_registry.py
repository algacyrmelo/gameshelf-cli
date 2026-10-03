from cmd_add import cmd_add
from cmd_exit import cmd_exit
from cmd_list import cmd_list
from cmd_rename import cmd_rename
from game_shelf import GameShelf


def cmd_help(shelf: GameShelf, *args: str) -> None:
    print()
    print("GameShelf CLI")
    print()
    for name, cmd in COMMANDS.items():
        print(f"- {name}: {cmd['desc']}")
    print()


COMMANDS = {
    "add": {"desc": "Add a new game", "callback": cmd_add},
    "list": {"desc": "List games", "callback": cmd_list},
    "help": {"desc": "Show command options", "callback": cmd_help},
    "exit": {"desc": "Exit gameshelf", "callback": cmd_exit},
    "rename": {"desc": "Rename game title", "callback": cmd_rename},
}
