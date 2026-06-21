from collections import deque
from typing import Deque, Dict, List, Optional, Tuple

from cell import directions, directions_letters
from maze_generator import Maze

Coord = Tuple[int, int]


class MazeSolver:

    def __init__(self, maze: Maze) -> None:
        self.maze = maze

    def _open_neighbors(
        self, row: int, col: int
    ) -> List[Tuple[int, int, int]]:
        
        cell = self.maze.cell_at(row, col)
        result: List[Tuple[int, int, int]] = []

        for direction, (drow, dcol) in directions.items():
            if cell.has_wall(direction):
                continue

            nrow, ncol = row + drow, col + dcol

            if self.maze.in_bounds(nrow, ncol):
                result.append((direction, nrow, ncol))

        return result

    def shortest_path(self) -> Optional[List[str]]:

        start_x, start_y = self.maze.entry
        end_x, end_y = self.maze.exit

        start: Coord = (start_y, start_x)
        end: Coord = (end_y, end_x)

        if not self.maze.in_bounds(*start) or not self.maze.in_bounds(*end):
            return None

        if start == end:
            return []

        visited = {start}
        queue: Deque[Coord] = deque([start])
        came_from: Dict[Coord, Tuple[Coord, int]] = {}

        while queue:
            row, col = queue.popleft()

            if (row, col) == end:
                return self._rebuild_path(came_from, start, end)

            for direction, nrow, ncol in self._open_neighbors(row, col):
                neighbor = (nrow, ncol)

                if neighbor in visited:
                    continue

                visited.add(neighbor)
                came_from[neighbor] = ((row, col), direction)
                queue.append(neighbor)

        return None

    @staticmethod
    def _rebuild_path(
        came_from: Dict[Coord, Tuple[Coord, int]],
        start: Coord,
        end: Coord,
    ) -> List[str]:
        
        path: List[str] = []
        current = end

        while current != start:
            previous, direction = came_from[current]
            path.append(directions_letters[direction])
            current = previous

        path.reverse()
        return path

    def path_to_string(self) -> str:

        path = self.shortest_path()
        if path is None:
            return ""
        return "".join(path)


def main() -> None:
    
    import sys

    from config_parser import config_file

    if len(sys.argv) != 2:
        print("Usage: python3 solver.py config.txt", file=sys.stderr)
        sys.exit(1)

    try:
        config = config_file(sys.argv[1])
        maze = Maze(config)
        maze.generate()

        solver = MazeSolver(maze)
        result = solver.shortest_path()
    except Exception as error:  # noqa: BLE001
        print(f"Error solving maze: {error}", file=sys.stderr)
        sys.exit(1)

    if result is None:
        print("No path found between entry and exit.")
    else:
        print("".join(result))


if __name__ == "__main__":
    main()