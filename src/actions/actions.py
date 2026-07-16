from random import shuffle


class Action:
    def __init__(self, game_map, simulation):
        self.game_map = game_map
        self.simulation = simulation

    def spawn(self):
        empty_cells = self.game_map.get_empty_cells()
        shuffle(empty_cells)
        y, x = empty_cells.pop()
        # Фактори:
        cur_obj = obj.create_obj(y, x)
        self.game_map.add_object(cur_obj)

    def map_update(self):
        pass
