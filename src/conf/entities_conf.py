from ..entities import Herbivore, Apple
from ..pathfinding import pathfinder_BFS
"""
Файл конфигурации объектов и их количество на карте.

CREATURE_CONF:
    "hp": 0 < INT <= 100 - Здоровье существа
    "speed": 0 < INT <= 3 - Скорость существа
    Оптионально только для хищников
    "attack": 0 < INT <= 100 - Сила атаки существа
    "target": цели, которые ищет существо

Количество объектов на карте:

OBJECT_POPULATION_CONF
    "Объект": INT - количество существ на карте

"""


# Конфигурация существ
HERBIVORE_CONF = {
    "hp": 100,
    "speed": 1,
    "nutrition": 50,
    "target": ["Apple"]
}

PREDATOR_CONF = {
    "hp": 100,
    "speed": 50,
    "attack": 50,
    "target": ["Herbivore"]
}

APPLE_CONF = {
   "nutrition": 50
}

CREATURE_PATHFINDER_CONF = {
    "pathfinder": pathfinder_BFS
}

# Конфигурация количества существ на карте
OBJECT_POPULATION_CONF = {
    "HERBIVORE": 5,
    "PREDATOR": 5,
    "APPLE": 5,
    "TREE": 5,
    "ROCK": 5
}
