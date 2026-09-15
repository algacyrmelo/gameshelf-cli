# GameShelf CLI

A place to keep the games I'm playing, have beaten or platinumed.


## Next implementations

- Create commands that changes the game status easily.
For example: `beat game_id`, `plat game_id`, `play game_id`, etc.

## User Stories

- Add a game
- Change a game's status
- List games
- Rename game title

## Technical Requirements

- Use unique numeric IDs
- Validate statuses: `playing`, `beaten`, `platinumed`, `dropped`, `endless`
- Preserve data between runs

## Data Model

```python
game = {
    "id": 1,
    "title": "Example Game",
    "status": "playing",
}
```
