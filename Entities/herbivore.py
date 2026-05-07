from Entities.creature import Creature

class Herbivore(Creature):

    def __init__(self, y, x, speed, hp, target):
        super().__init__(y, x, speed, hp)
        self.target = target

    def __str__(self):
        return "🐰"


       
                
