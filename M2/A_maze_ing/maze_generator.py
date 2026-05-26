from cell import Cell, north, south, east, west, walls
from cell import directions, opposite_directions
from config_parser import config_file, ConfigMaze


class Maze:
    widht: int
    height: int
    entry: tuple[int, int]
    exit: tuple[int, int]
    grid: list[list[Cell]]

    def __init__(self, config: ConfigMaze) -> None:
        self.width = config.WIDTH
        self.height = config.HEIGHT
        self.entry = config.ENTRY
        self.exit = config.EXIT
        self.grid = [
            [Cell(row=r, col=c) for c in range(self.width)]
            for r in range(self.height)
        ]
