from game_map import Map
from actions.action import Action

class Map_update(Action):
    def __init__(self, map: Map):
        self.map = map
    
    def run(self):
        
        for y in range(self.map.height):
            for x in range(self.map.width):
                self.map.grid[y][x] = None

        for obj in self.map.objects:
            self.map.grid[obj.y][obj.x] = obj

        
        
                