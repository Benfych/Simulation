from

class Next_move(Action):
    def __init__(self, game_map):
        self._game_map = game_map

    def run(self):
        self.simulation._move_counter += 1
        is_creature = lambda obj: is_instance(obj, Creature)
        for obj in filter(is_creature, object):
            obj.make_move(self.pathfinding, self.map, self.eat_action, self.simulation._move_counter)