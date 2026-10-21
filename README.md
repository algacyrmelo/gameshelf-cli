# GameShelf CLI

A place to keep the games I'm playing, have beaten or platinumed.

## Usage

```bash
python3 main.py
```

## Testing

```bash
chmod +x ./test.sh
./test.sh
```

## Next implementations

- [ ] Add persistence
- [ ] Create commands that changes the game status easily.
For example: `beat game_id`, `plat game_id`, `play game_id`, etc.

## User Stories

- Add a game
- Change a game's status
- List games
- Rename game title

## Technical Requirements

- Unique numeric IDs
- Validate statuses: `playing`, `beaten`, `platinumed`, `dropped`, `endless`
- Preserve data between runs

## Data Model

```python
@dataclass
class Game:
    id: int
    title: str
    status: GameStatus = GameStatus.PLAYING
```

## Persistence

Data is stored as a single JSON file.

```json
{
    "next_id": 3,
    "games": [
        {"id": 1, "title": "Celeste": "status": "playing"},
        {"id": 2, "title": "A Mortician's Tale": "status": "beaten"}
    ]
}
```

`status` is saved as text (the enum value).

If the file does not exist, start with an empty shelf.
