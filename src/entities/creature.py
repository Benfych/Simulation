from random import randint

from .entity import Entity


class Creature(Entity):
    """
    Родительский класс существ, обладающий базовым функционал


    """

    def __init__(self, cord, hp, speed, pathfinder):
        super().__init__(cord)
        self._moves = []
        self._speed = speed
        self._hp = hp
        self._hungry = 100
        self._target = target
        self._pathfinder = patchfinder
        self._move_counter = 0

    def make_move(self, pathfinding, move_counter):
        self._move_counter += 1

        if self.hungry < 100:

            self.moves = pathfinding.get_moves(self.x, self.y, self.target)

            if self.moves:
                if self.speed >= len(self.moves):
                    self.moves = [self.moves[0]]
                else:
                    self.moves = self.moves[::self.speed]

                ny, nx = self.moves.pop()

                if (isinstance(map.grid[ny][nx], (self.target, None))):
                    self.y, self.x = ny, nx
                    if isinstance(map.grid[self.y][self.x], self.target):
                        eat_action.run(self, self.target)
                else:
                    self.moves = []

    def update_state(self):
        if self._hp <= 0:
            self._to_remove()
        if self._move_counter % 2 == 0:
            self.take_hunger()
        if self.hungry == 0 or self.hungry < 0:
            self._to_remove()

    def eat(self, target):
        if (100 - obj.hungry) <= 50:
            self.hungry += (100 - self.hungry)
        else:
            self.hungry += 50

        target.remove_entity()

    def take_damage(self, count):
        self._hp -= count

    def take_hunger(self, move_counter):
        self._hunger -= 5
