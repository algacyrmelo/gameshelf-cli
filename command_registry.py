from cmd_add import cmd_add
from cmd_exit import cmd_exit
from cmd_list import cmd_list
from cmd_rename import cmd_rename


def get_commands():
    return {
        "add": {"desc": "Add a new game", "callback": cmd_add},
        "list": {"desc": "List games", "callback": cmd_list},
        "help": {"desc": "Show command options", "callback": cmd_help},
        "exit": {"desc": "Exit gameshelf", "callback": cmd_exit},
        "rename": {"desc": "Rename game title", "callback": cmd_rename},
    }


def cmd_help(shelf, *args):
    print()
    print("GameShelf CLI")
    print()
    for name, desc in list_commands():
        print(f"- {name}: {desc}")
    print()


def list_commands() -> list[tuple]:
    return [
        (name, cmd["desc"], cmd["callback"]) for name, cmd in get_commands().items()
    ]
