from dataclasses import dataclass
from Entities.entity import Entity
from Entities.predator import Predator
from cfg.cfg import Cfg

@dataclass
class Predator_cfg(Cfg):
    target: Entity
    speed: int = 1
    hp: int = 100
    name = "Predator"

    def create_obj(self, x, y):
        return Predator(x, y, self.speed, self.hp, self.target)

