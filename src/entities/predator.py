from creature import Creature


class Predator(Creature):
    def __init__(self, y, x, speed, health, target):
        super().__init__(y, x, speed, health, target)
