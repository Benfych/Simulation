from abc import ABC, abstractmethod
from random import randint

from .entity import Entity


class Creature(ABC, Entity):
    """
    Базовый класс для всех существ симуляции.

    Определяет общий контракт поведения: движение, голод, здоровье,
    взаимодействие с другими существами. Конкретные типы существ

    Attributes:
        _hp (int): текущее здоровье.
        _hungry (int): текущий уровень голода (0 — смерть).
        _speed (int): сколько клеток проходит за ход.
        _target (list[str]): имена классов, с которыми существо
        _moves (list): текущий путь до цели.
        _creature_move_counter (int): счётчик ходов для периодических эффектов.

    """

    def __init__(self, y, x, hp, speed, target):
        super().__init__(y, x)
        self._moves = []
        self._speed = speed
        self._hp = hp
        self._hungry = 100
        self._target = target
        self._creature_move_counter = 0

    def make_move(self, game_map, pathfinder):
        self._creature_move_counter += 1
        self.update_state()

        if self._hungry < 100:
            self.moves = pathfinder.get_moves(self._y, self._x, self._target)
            if self.moves:
                if self._speed >= len(self.moves):
                    self.moves = [self.moves[0]]
                else:
                    self.moves = self.moves[::self._speed]

                ny, nx = self.moves.pop()
                if game_map.is_free(ny, nx):
                    game_map.move_object(self._y, self._x, ny, nx, self)
                    self._y, self._x = ny, nx
                else:
                    self.moves = []

                #Каждый ход, существо проверяет клетки вокруг себя на наличие цели
                #при нахождении, взаимодействует с ней
                directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                for dy, dx in directions:
                    if 0 <= self._y + dy < game_map.get_height() and 0 <= self._x + dx < game_map.get_width():
                        cell = game_map.get_object(self._y + dy, self._x + dx)
                        if any(cell.__class__.__name__ == t for t in self._target):
                            self.target_interaction(cell)

    #Обновление статуса существа каждый ти
    def update_state(self):
        if self._hp <= 0:
            self.to_remove()
        if self._creature_move_counter % 2 == 0:
            self.take_hunger(10)
        if self._hungry == 0 or self._hungry < 0:
            self.take_damage(10)

    def eat(self, obj):
        count = obj.on_eat()
        if (100 - self._hungry) <= 50:
            self.take_hunger(count - self._hungry)
        else:
            self.take_hunger(count)

    @abstractmethod
    def target_interaction(self, obj):
        """
        Абастрактный метод взаимодействия существа с целью
        Реализуется каждым существом по своему, к примеру:
            Herbivore - кушает цель сразу, потому что питается фруктами
            Predator - сначала атакует, затем ест цель после её гибели

        """
        pass

    def get_hp(self):
        return self._hp

    def get_hungry(self):
        return self._hungry

    def get_nutritional(self):
        return self._nutritional

    def take_damage(self, count):
        self._hp -= count

    def take_hunger(self, count):
        self._hungry -= count

