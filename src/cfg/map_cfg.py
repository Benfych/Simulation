from dataclasses import dataclass


@dataclass
class MapCfg:
    pathfinder: type[pathfinder]
    height: int = 20
    width: int = 20
