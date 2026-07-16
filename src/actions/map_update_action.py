from actions import Action
from game_map import GameMap


class Map_update(Action):
    def __init__(self, game_map):
        self.game_map = game_map

    def run(self):
        self.game_map.map_update()
