from dataclasses import dataclass
from Entities.apple import Apple
from cfg.cfg import Cfg

@dataclass
class Apple_cfg(Cfg):
    name = "Apple"

    def create_obj(self, y, x):
        return Apple(y, x)


