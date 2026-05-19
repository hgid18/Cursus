from typing import Dict, Any, Tuple, Optional
import sys


class ConfigMaze:
    WIDTH: int
    HEIGHT: int
    ENTRY: tuple[int, int]
    EXIT: tuple[int, int]
    PERFECT: str
    SEED: Optional[int]


def coords_parser(key: str) -> tuple[int, int]:
    coords = key.split(",")
    try:
        coord1 = int(coords[0].strip)
        coord2 = int(coords[1].strip)
    except ValueError:
        raise ValueError(
            f"Invalid coordinates format: {key}."
            "Coordinates must be integers.")
    return (coord1, coord2)
