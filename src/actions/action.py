from ABS import ABS


class Action(ABC):
    """абстрактный класс для action"""
    @abstractmethod
    def execute(self, game_map):
        pass
