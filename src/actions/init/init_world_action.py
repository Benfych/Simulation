from ...conf import OBJECT_COUNT_CONF
from ...service import SpawnerService
from ..action import Action

class InitWorldAction(Action):
    def __init__(self, game_map):
        self._game_map = game_map
        self._object_count_conf = OBJECT_COUNT_CONF
        self._start = 0

    def execute(self):
        self._start += 1
        for obj in self._object_count_conf:
            for obj_count in range(self._object_count_conf[obj]):
                SpawnerService.spawn(self._game_map, obj)


    