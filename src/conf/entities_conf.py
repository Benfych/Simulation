from entities import herbivore, apple

"""
Файл конфигурации объектов и их количество на карте.

CREATURE_CONF:
    "hp": 0 < INT <= 100 - Здоровье существа
    "speed": 0 < INT <= 3 - Скорость существа
    Оптионально только для хищников
    "attack": 0 < INT <= 100 - Сила атаки существа
    "target

Количество объектов на карте:

OBJECT_POPULATION_CONF
    "Объект": INT - количество существ на карте

"""


# Конфигурация существ
HERBIVORE_CONF = {
    "hp": 100,
    "speed": 1,
    "target": [apple]
}

PREDATOR_CONF = {
    "hp": 100,
    "speed": 1,
    "attack": 50,
    "target": [herbivore]
}

CREATURE_PATHFINDER_CONF = {
    "pathfinder": "PathFinderBFS"
}

# Конфигурация количества существ на карте
OBJECT_POPULATION_CONF = {
    "HERBIVORE": 5,
    "PREDATOR": 5,
    "APPLE": 5,
    "TREE": 5,
    "ROCK": 5
}
