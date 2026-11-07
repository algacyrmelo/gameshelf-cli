from typing import TypedDict


class GameDict(TypedDict):
    id: int
    title: str
    status: str


class ShelfDict(TypedDict):
    next_id: int
    games: list[GameDict]
