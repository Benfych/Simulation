from Entities.creature import Creature


class Predator(Creature):
    def __init__(self, y, x, speed, hp, target):
        super().__init__(y, x, speed, hp, target)
