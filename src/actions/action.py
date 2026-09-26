from abc import ABC, abstractmethod

class Action(ABC):
    """абстрактный класс для action"""

    @abstractmethod
    def execute(self, game_map):
        pass
