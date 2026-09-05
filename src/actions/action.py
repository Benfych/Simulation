from abc import ABC, abstractmethod


# Абстрактный класс для actions
class Action(ABC):
    @abstractmethod
    def run():
        pass
