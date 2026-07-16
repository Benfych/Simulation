from random import randint
from collections import deque
from Entities import Rock
from Entities import Tree
from game_map import GameMap


class BFS:
    def __init__(self, game_map):
        self.game_map = game_map
        self.visited = set()
        self.parents = {}
        self.queue = deque()
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.rows = self.game_map.get_width
        self.col = self.game_map.get_height

    def get_moves(self, start_y: int, start_x: int, target) -> list:
        self.queue = deque([(start_y, start_x)])
        self.visited = {(start_y, start_x)}
        self.parents = {}

        while self.queue:
            y, x = self.queue.popleft()

            if isinstance(self.game_map.get_cell(y, x), target):
                path = []
                current = (y, x)

                while current != (start_y, start_x):
                    path.append(current)
                    current = self.parents[current]
                return path

            for dy, dx in self.directions:
                ny, nx = y + dy, x + dx
                if (
                    0 <= nx < self.rows
                    and 0 <= ny < self.col
                    and (ny, nx) not in self.visited
                ):
                    if not isinstance(
                        self.game_map.get_cell(ny, nx), Rock
                    ) and not isinstance(self.game_map.get_cell(ny, nx), Tree):
                        self.visited.add((ny, nx))
                        self.parents[(ny, nx)] = (y, x)
                        self.queue.append((ny, nx))

        return []
