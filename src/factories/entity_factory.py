from entities import Apple, Herbivore, Predator, Rock, Tree

# Импорт конифгов
from conf import HERBIVORE_CONF, PREDATOR_CONF, TREE_CONF, APPLE_CONF, ROCK_CONF, MAP_CONF


class EntityFactory:
    """Простая фабрика для создания экземпляров объектов"""
    @classmethod
    def create_entity(entity_type, x, y):
        match entity_type:
            case "Apple":
                return Apple(x, y, APPLE_CONF)
            case "Herbivore":
                return Herbivore(x, y, HERBIVORE_CONF)
            case "Predator":
                return Predator(x, y, PREDATOR_CONF)
            case "Rock":
                return Rock(x, y, ROCK_CONF)
            case "Tree":
                return Tree(x, y, TREE_CONF)
            case _:
                raise ValueError(f"Неизвестный тип: {entity_type}")
