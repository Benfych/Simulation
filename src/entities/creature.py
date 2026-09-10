from random import randint

from .entity import Entity


class Creature(Entity):
    """
    Родительский класс существ, обладающий базовым функционал


    """

    def __init__(self, cord, hp, speed, target, pathfinder):
        super().__init__(cord)
        self._moves = []
        self._speed = speed
        self._hp = hp
        self._hungry = 100
        self._target = target
        self._pathfinder = pathfinder
        self._move_counter = 0

    def make_move(self, pathfinding):
        self.update_state()
        self._move_counter += 1

        if self._hungry < 100:

            self.moves = pathfinding.get_moves(self.x, self.y, self._target)

            if self.moves:
                if self.obj

                if self._speed >= len(self.moves):
                    self.moves = [self.moves[0]]
                else:
                    self.moves = self.moves[::self._speed]

                ny, nx = self.moves.pop()

                if (isinstance(map.grid[ny][nx], (self.target, None))):
                    self.y, self.x = ny, nx
                    if isinstance(map._grid[self.y][self.x], self._target):
                        self.eat(target)
                else:
                    self.moves = []


    def update_state(self):
        if self._hp <= 0:
            self.remove_entity()
        if self._move_counter % 2 == 0:
            self.take_hunger()
        if self._hungry == 0 or self._hungry < 0:
            self.remove_entity()

    def eat(self, target):
        if (100 - self._hungry) <= 50:
            self._hungry += (100 - self._hungry)
        else:
            self._hungry += 50

        target.remove_entity()

    def take_damage(self, count):
        self._hp -= count

    def take_hunger(self):
        self._hungry -= 5
