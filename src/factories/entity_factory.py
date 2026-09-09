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
    @classmethod
    def create_entity(entity_type, cord, config):
        match entity_type:
            case "Apple":
                return Apple(cord, config)
            case "Herbivore":
                return Herbivore(cord, config)
            case "Predator":
                return Predator(cord, config)
            case "Rock":
                return Rock(cord, config)
            case "Tree":
                return Tree(cord, config)
            case "EmptyCell":
                return EmptyCell(cord, config)
            case _:
                raise ValueError(f"Неизвестный тип: {entity_type}")
