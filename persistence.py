import json
from pathlib import Path

from shelf import Shelf
from conversion import shelf_from_dict, shelf_to_dict

DATA_FILE = Path.home() / ".gameshelf" / "shelf.json"


def load(fp: Path) -> Shelf:
    if not fp.exists():
        return Shelf()

    print(f"Loading data from {fp}")
    with open(fp) as f:
        data = json.load(f)

    shelf = shelf_from_dict(data)
    return shelf


def save(shelf: Shelf, fp: Path) -> None:
    if not fp.parent.exists():
        fp.parent.mkdir()

    print(f"Saving data changes at {fp}")
    with open(fp, "w") as f:
        shelf_data = shelf_to_dict(shelf)
        json.dump(shelf_data, f)
