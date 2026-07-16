class Spawner:
    def __init__(self, game_map):
        self.game_map: game_map = game_map

    def run(self, obj):
        empty_cells = self.game_map.get_empty_cells()
        # shuffle(empty_cells)
        y, x = empty_cells.pop()
        cur_obj = obj.create_obj(y, x)
        self.game_map.add_object(cur_obj)
