from ..entities import Apple, Herbivore, Predator, Rock, Tree
from ..conf import HERBIVORE_CONF, PREDATOR_CONF, MAP_CONF, APPLE_CONF


class EntityFactory:
    """Простая фабрика для создания экземпляров объектов"""

    @staticmethod
    def create_entity(entity_type, y, x):
        if entity_type == "Apple":
            return Apple(y, x, APPLE_CONF)
        elif entity_type == "Herbivore":
            return Herbivore(y, x, HERBIVORE_CONF)
        elif entity_type == "Predator":
            return Predator(y, x, PREDATOR_CONF)
        elif entity_type == "Rock":
            return Rock(y, x)
        elif entity_type == "Tree":
            return Tree(y, x)
        else:
            raise ValueError(f"Неизвестный тип: {entity_type}")
