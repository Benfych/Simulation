from dataclasses import dataclass

@dataclass
class HerbivoreCfg:
    speed = 1
    hp = 100
    amount = 5
    target = ("Apple",)
    name = "Herbivore"

