from .creature import Creature


class Herbivore(Creature):
    def __init__(self, cord, conf):
        hp = conf["HP"]
        speed = conf["SPEED"]
        target = conf["TARGET"]
        super().__init__(cord, hp, speed, target)

