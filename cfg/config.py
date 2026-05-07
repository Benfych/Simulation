from cfg.map_cfg import Map_cfg

from cfg.predator_cfg import Predator_cfg
from cfg.herbivore_cfg import Herbivore_cfg
from cfg.apple_cfg import Apple_cfg
from cfg.tree_cfg import Tree_cfg
from cfg.rock_cfg import Rock_cfg
from Entities.apple import Apple
from Entities.herbivore import Herbivore
from patchfinding.BFS import BFS


# Файл с настройкой конфигов:
# ------------------Карта-----------------------
MAP_DEFAULT_CONFIG = Map_cfg(20, 20, BFS)

# ----------------------------------------------


# ------------------МОБЫ-----------------------
PREDATOR_DEFAULT_CONFIG = Predator_cfg(5, (Herbivore), 1, 100)
HERBIVORE_DEFAULT_CONFIG = Herbivore_cfg(5, (Apple), 1, 100)
APPLE_DEFAULT_CONFIG = Apple_cfg(5)
TREE_DEFAULT_CONFIG = Tree_cfg(10)
ROCK_DEFAULT_CONFIG = Rock_cfg(5)
# ----------------------------------------------



