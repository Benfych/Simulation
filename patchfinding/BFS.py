from random import randint
from collections import deque
from Entities.rock import Rock
from Entities.tree import Tree

class BFS:
    # target: Entity
    def __init__(self, map: Map):
        self.map = map
        self.visited = set()
        self.parents = {}
        self.queue = deque()
        self.directions = [(1, 0),(0, 1),(-1, 0),(0, -1)]
        self.rows = len(self.map.get_grid[0])
        self.col = len(self.map.get_grid)
        
    def get_moves(self, start_y: int, start_x: int, target) -> list:
        self.queue = deque([(start_y, start_x)])
        self.visited = {(start_y, start_x)}
        self.parents = {}

        while self.queue:
            y, x = self.queue.popleft()

            if isinstance(self.map.get_grid[y][x], target):
                path = []
                current = (y, x)
                
                while current != (start_y, start_x):
                    path.append(current)
                    current = self.parents[current]
                
                # path.reverse()
                return path
        
            for dy, dx in self.directions:
                ny, nx = y + dy, x + dx
                if 0 <= nx < self.rows and 0 <= ny < self.col and (ny, nx) not in self.visited:
                    if not isinstance(self.map.get_grid[ny][nx], Rock) and not isinstance(self.map.get_grid[ny][nx], Tree):
                        self.visited.add((ny, nx))
                        self.parents[(ny, nx)] = (y, x)
                        self.queue.append((ny, nx))
                        
                        
                    

                                            




                
        
        









        # self.target: entity
    
        # self.moves = []
        # self.default_position = default_position

        # for _ in range(5):
        #     x, y = self.default_position
        #     dx, dy = x + randint(-1, 1), y + randint(-1, 1)
        #     self.moves.append((dx, dy))

        # return self.moves
            
            




