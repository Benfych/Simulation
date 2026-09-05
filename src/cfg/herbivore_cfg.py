from dataclasses import dataclass
from Entities.apple import Apple
from Entities.herbivore import Herbivore
from cfg.cfg import Cfg

@dataclass
class Herbivore_cfg(Cfg):
    target: list
    speed: int = 1
    hp: int = 100
    name = "Herbivore"

    def create_obj(self, x, y):
        return Herbivore(x, y, self.speed, self.hp, self.target)
    
