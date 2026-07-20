from dataclasses import dataclass


@dataclass
class PredatorCfg:
    target: tuple = ("Herbivore",)
    speed: int = 1
    hp: int = 100
    count: int = 5
