from .apple import Apple
from .herbivore import Herbivore
from .predator import Predator
from .rock import Rock
from .tree import Tree
from .empty_cell import EmptyCell

# Импорт конифгов
from conf import RABBIT_CONF, WOLF_CONF, TREE_CONF, APPLE_CONF, ROCK_CONF, MAP_CONF


class EntityFactory:
    """Простая фабрика для создания экземпляров объектов"""

    @classmethod
    def create_entity(cls, entity_type):

        match entity_type:
            case "Apple":
                return Apple(APPLE_CONF["COUNT"])
            case "Herbivore":
                return Herbivore(HERBIVORE_CONF["COUNT"])
            case "Predator":
                return Predator(cls.map_conf)
            case "Rock":
                return Rock(cls.map_conf)
            case "Tree":
                return Tree(cls.map_conf)
            case "EmptyCell":
                return EmptyCell(cls.map_conf)
            case _:
                raise ValueError(f"Неизвестный тип: {entity_type}")
