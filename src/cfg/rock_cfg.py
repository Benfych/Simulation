from dataclasses import dataclass
from Entities.rock import Rock 
from cfg.cfg import Cfg

@dataclass
class Rock_cfg(Cfg):
    name = "Rock"

    def create_obj(self, y, x):
        return Rock(y, x)