"""
Файл конфигурации объектов и их количество на карте.

CREATURE_CONF:
    "HP": 0 < INT <= 100 - Здоровье существа
    "SPEED": 0 < INT <= 3 - Скорость существа
    Оптионально только для хищников
    "ATTACK": 0 < INT <= 100 - Сила атаки существа


Количество объектов на карте:

OBJECT_POPULATION_CONF
    "Объект": INT - количество существ на карте

"""


#Конфигурация существ
HERBIVORE_CONF = {
    "HP": 100,
    "speed": 1,
}

PREDATOR_CONF = {
    "HP": 100,
    "speed": 1,
    "attack": 50,
}

#Конфигурация количества существ на карте
OBJECT_POPULATION_CONF = {
    "HERBIVORE": 5,
    "PREDATOR": 5,
    "APPLE": 5,
    "TREE": 5,
    "ROCK": 5
}
