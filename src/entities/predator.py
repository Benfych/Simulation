from Entities.creature import Creature
from .herbivore import Herbivore

class Predator(Creature):
    def __init__(self, x, y, speed, hp, patchfinder) :
        target = Herbivore
        super().__init__(x, y, speed, hp, target, patchfinder)
