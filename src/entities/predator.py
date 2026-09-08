from Entities.creature import Creature
from .herbivore import Herbivore
from conf import PREDATOR_CONF


class Predator(Creature):
    def __init__(self, cord, config):
        super().__init__(x, y, HP, SPEED)
