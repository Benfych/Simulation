from .creature import Creature


class Predator(Creature):
    """
     Хищник — существо, которое охотится на других существ.

     Наследуется от Creature. Отличается наличием силы атаки
     и поведением target_interaction: вместо поедания цели
     хищник наносит ей урон, а если цель погибает — съедает.

     Attributes:
         _attack (int): сила атаки. Наносится цели при взаимодействии.
         _hp (int): здоровье хищника.
         _speed (int): скорость передвижения.
         _target (list[str]): имена классов, на которые охотится хищник
     """


    def __init__(self, y, x, conf):
        self._hp = conf["hp"]
        self._speed = conf["speed"]
        self._attack = conf["attack"]
        self._target = conf["target"]
        super().__init__(y, x, self._hp, self._speed, self._target)

    def target_interaction(self, obj):
        if 0 < obj.get_hp() <= 100:
            obj.take_damage(self._attack)
            if obj.get_hp() <= 0:
                self.eat(obj)

