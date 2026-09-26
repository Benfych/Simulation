from .entity import Entity
from .edible import Edible

class Apple(Entity, Edible):
    """
    Яблоко - объект которым питаются травоядные
    Attributes:
    _nutrition (int): питательная ценность

    """
    def __init__(self, y, x, conf):
        self._nutrition = conf["nutrition"]
        Entity.__init__(self, y, x)
        Edible.__init__(self, self._nutrition)

