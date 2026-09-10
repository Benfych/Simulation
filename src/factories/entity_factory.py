from .apple import Apple
from entities.herbivore import Herbivore
from .predator import Predator
from .rock import Rock
from .tree import Tree
from .empty_cell import EmptyCell

# Импорт конифгов
from conf import HERBIVORE_CONF, PREDATOR_CONF, TREE_CONF, APPLE_CONF, ROCK_CONF, MAP_CONF


class EntityFactory:
    """Простая фабрика для создания экземпляров объектов"""
    @classmethod
    def create_entity(entity_type, x, y):
        match entity_type:
            case "Apple":
                return Apple(x, y, config)
            case "Herbivore":
                return Herbivore(x, y, HERBIVORE_CONF)
            case "Predator":
                return Predator(x, y, PREDATOR_CONF)
            case "Rock":
                return Rock(x, y, config)
            case "Tree":
                return Tree(x, y, config)
            case "EmptyCell":
                return EmptyCell(x, y, config)
            case _:
                raise ValueError(f"Неизвестный тип: {entity_type}")
