from random import shuffle
from game_map import Map


class Spawner:
    def __init__(self, map):
        self.map = map

    def run(self, obj):
        empty_cells = self.map.get_empty_cells()
        shuffle(empty_cells)
        y, x = empty_cells.pop()
        cur_obj = obj.create_obj(y, x)
        self.map.add_object(cur_obj)
