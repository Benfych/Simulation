from Entities.creature import Creature

class Predator(Creature):
    def __init__(self, cord, conf):
        HP = conf[HP]
        SPEED = conf[SPEED]
        ATTACK = conf[ATTACK]
        super().__init__(cord, HP, SPEED)

