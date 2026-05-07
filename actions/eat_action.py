from Entities import creature
from actions.action import Action
from game_map import Map


class Eat_action(Action):
    def __init__(self, map: Map):
        self.map = map
    
    def run(self, obj, target):
        if (100 - obj.hungry) <= 50:  
            obj.hungry += (100 - obj.hungry)
        else:
            obj.hungry += 50
        
        target_rm = [target
        for target in self.map.get_objects
        if isinstance(target, obj.target) 
        and obj.x == target.x 
        and obj.y == target.y]

        if target_rm:
            target_rm = target_rm[0]
        else:
            return 

        self.map.remove_object(target_rm)
        
        


