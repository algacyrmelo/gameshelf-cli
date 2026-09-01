# GameShelf CLI

A place to keep the games I'm playing, have beaten or platinumed.

## User Stories

- Add a game
- Change a game's status
- List games
- Edit or delete game data

## Technical Requirements

- Use unique numeric IDs
- Validate statuses: `playing`, `beaten`, `platinumed`, `endless`
- Preserve data between runs
- Game titles must be unique

## Data Model

```python
game = {
    "id": 1,
    "title": "Example Game",
    "status": "playing",
}
```
