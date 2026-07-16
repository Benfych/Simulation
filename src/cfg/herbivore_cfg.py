from dataclasses import dataclass

@dataclass
class HerbivoreCfg:
    speed: int = 1
    hp: int = 100
    amount: int = 5
    target: tuple = ("Apple",)
    name: str = "Herbivore"

