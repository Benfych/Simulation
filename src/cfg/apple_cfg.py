from dataclasses import dataclass
from entities import Apple


@dataclass
class AppleCfg:
    amount: int = 5
    name: str = "Apple"
