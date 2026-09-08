from .creature import Creature
from conf import HERBIVORE_CONF


class Herbivore(Creature):
    def __init__(self):
        HP = HERBIVORE_CONF["HP"]
        SPEED = HERBIVORE_CONF["SPEED"]

        super().__init__(x, y, speed, hp, target, patchfinding)
        
