from game_map import Map
from actions.action import Action

class Map_update(Action):
    def __init__(self, map: Map):
        self.map = map
    
    def run(self):
        
        for y in range(self.map.get_height):
            for x in range(self.map.get_width):
                self.map.get_grid[y][x] = None

        for obj in self.map.get_objects:
            self.map.get_grid[obj.y][obj.x] = obj

        
        
                