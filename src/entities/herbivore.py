from .creature import Creature


class Herbivore(Creature):
    def __init__(self, cord, conf):
        HP = conf["HP"]
        SPEED = conf["SPEED"]
        TARGET = conf["TARGET"]
        super().__init__(cord, HP, SPEED, TARGET)
