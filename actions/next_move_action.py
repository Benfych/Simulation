from actions.action import Action
from actions.eat_action import Eat_action
from actions.map_update_action import Map_update
from game_map import Map

class Next_move(Action):
    def __init__(self, map: Map, simulation):
        self.map = map
        self.objects = self.map.objects
        self.pathfinding = self.map.pathfinding
        self.eat_action = Eat_action(self.map)
        self.simulation = simulation
        
    def run(self):
        self.simulation._move_counter += 1
        for obj in self.objects:
            obj.update(self.pathfinding, self.map, self.eat_action, self.simulation._move_counter)