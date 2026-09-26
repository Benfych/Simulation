from ..action import Action
from ...entities import Creature

class NextMoveAction(Action):
    """

    Action, который заставляет существ сделать следующий ход
    итерируясь по каждому и вызывая метод make_move.

    Attributes:
        _objects (list): получает копию списка ссылок на объекты

    """
    def __init__(self, game_map, pathfinder):
        self._game_map = game_map
        self._pathfinder = pathfinder
        self._objects = None

    def execute(self):
        self._objects = self._game_map.get_objects()
        it_creature = lambda x: isinstance(x, Creature)
        for obj in filter(it_creature, self._objects):
            obj.make_move(self._game_map, self._pathfinder)
