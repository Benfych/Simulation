from .apple import Apple
from entities.herbivore import Herbivore
from .predator import Predator
from .rock import Rock
from .tree import Tree
from .empty_cell import EmptyCell

# Импорт конифгов
from conf import RABBIT_CONF, WOLF_CONF, TREE_CONF, APPLE_CONF, ROCK_CONF, MAP_CONF, HERBIVORE_CONF


class EntityFactory:
    """Простая фабрика для создания экземпляров объектов"""
    super().__init__(x, y, speed, hp, target, patchfinding)

    @classmethod
    def create_entity(entity_type, x, y):

        match entity_type:
            case "Apple":
                return Apple(x, y, APPLE_CONF["COUNT"])
            case "Herbivore":
                return Herbivore(x, y, HERBIVORE_CONF["SPEED"], HERBIVORE_CONF["HP"], HERBIVORE_CONF["PATHFINDING"])
            case "Predator":
                return Predator(x, y)
            case "Rock":
                return Rock(x, y)
            case "Tree":
                return Tree(x, y)
            case "EmptyCell":
                return EmptyCell(x, y)
            case _:
                raise ValueError(f"Неизвестный тип: {entity_type}")
