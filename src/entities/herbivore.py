from .creature import Creature
from .edible import Edible


class Herbivore(Creature, Edible):
    """
    Травоядное — существо, которое питается объектами-едой.

    Наследуется от Creature (поведение, движение, голод) и Edible
    (может быть съедено хищником). Взаимодействует с целью поеданием:
    вызывает on_eat() у цели и восстанавливает голод.

    Attributes:
        _hp (int): здоровье травоядного.
        _speed (int): скорость передвижения.
        _target (list[str]): имена классов, которые травоядное ест
        _nutrition (int): питательная ценность самого травоядного
    """

    def __init__(self, y, x, conf):
        self._hp = conf["hp"]
        self._speed = conf["speed"]
        self._target = conf["target"]
        self._nutrition = conf["nutrition"]
        Creature.__init__(self, y, x, self._hp, self._speed, self._target)
        Edible.__init__(self, self._nutrition)

    def target_interaction(self, obj):
        self.eat(obj)
