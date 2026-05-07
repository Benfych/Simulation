from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Cfg(ABC):
    count: int

    @abstractmethod
    def create_obj(self):    
        pass