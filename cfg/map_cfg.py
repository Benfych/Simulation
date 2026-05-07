from dataclasses import dataclass
from game_map import Map
from cfg.cfg import Cfg
from patchfinding.BFS import BFS

@dataclass
class Map_cfg():
    height: int
    width: int
    pathfinder: BFS


