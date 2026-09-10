from Entities.creature import Creature

class Predator(Creature):
    def __init__(self, cord, conf):
        hp = conf["hp"]
        speed= conf["speed"]
        attack = conf["attack"]
        super().__init__(cord, hp, speed)


    def attack(self, obj):
        obj.take_damage(self.attack)