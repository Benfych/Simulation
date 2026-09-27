from collections import deque
from ..entities import Rock
from ..entities import Tree


class PathfinderBFS:
    def __init__(self, game_map):
        self._game_map = game_map
        self._directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self._rows = self._game_map.get_height()
        self._cols = self._game_map.get_width()

    def get_moves(self, start_y, start_x, target):
        self.queue = deque([(start_y, start_x)])
        self.visited = {(start_y, start_x)}
        self.parents = {}

        while self.queue:
            y, x = self.queue.popleft()

            if any(self._game_map.get_object(y, x).__class__.__name__ == obj for obj in target):
                path = []
                current = (y, x)
                while current != (start_y, start_x):
                    path.append(current)
                    current = self.parents[current]
                return path

            for dy, dx in self._directions:
                ny, nx = y + dy, x + dx
                if 0 <= ny < self._rows and 0 <= nx < self._cols and (ny, nx) not in self.visited:
                    if not self._game_map.is_valid(ny, nx, Rock) and not self._game_map.is_valid(ny, nx, Tree):
                        self.visited.add((ny, nx))
                        self.parents[(ny, nx)] = (y, x)
                        self.queue.append((ny, nx))
