from ..action import Action
from ...conf import OBJECT_COUNT_CONF
from ...service import SpawnerService


class EntitiesRespawnAction(Action):
    """

    Action отвечающий за контроль популяцииа в симуляции
    Сверяет актуальное количесто объектов на карте с заданым в конфигурации,
    при расхождении количества вызывает SpawnerService() для восполнения недостающих
    с передачей типа объекта

    """
    def __init__(self, game_map):
        self._game_map = game_map
        self._object_count_conf = OBJECT_COUNT_CONF

    def execute(self):
        for obj in self._object_count_conf:
            if self._object_count_conf[obj] > self._game_map.get_objects_count(obj):
                SpawnerService.spawn(self._game_map, obj)


