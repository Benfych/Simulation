# реализовать удаление сущностей согласно ревью
from ..action import Action


class EntityRemoverAction(Action):
    """

    Action отвечающий за очистку карты от объектов с флагом to_remove = 1
    Получает список с копией ссылок на объектыа на карте, проверяет статус флага: obj.get_remove_status()
    при положительном результате, отправляет объект на удаление: game_map.remove_object(obj)

    """
    def __init__(self, game_map, pathfinder):
        self._game_map = game_map
        self._objects = None

    def execute(self):
        self.objects = self._game_map.get_objects()
        for obj in self.objects:
            if obj.get_remove_status():
                self._game_map.remove_object(obj)
