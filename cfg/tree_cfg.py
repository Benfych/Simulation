from dataclasses import dataclass
from Entities.tree import Tree 
from cfg.cfg import Cfg

@dataclass
class Tree_cfg(Cfg):
    name = "Tree"

    def create_obj(self, y, x):
        return Tree(y, x)