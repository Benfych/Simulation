from random import randint


def SpawnAction(Action):
    """спавнер объектов на карте"""

    def execute(self, game_map, obj):
        nx, xy = randint(0, self.width - 1), randint(0, self.height - 1)
        game_map.

