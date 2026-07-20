from entity import Entity


class Creature(Entity):
    def __init__(self, y, x, speed, health, target):
        super().__init__(y, x)
        self.speed = speed
        self.health = health
        self.hungry = 100
        self.moves = []
        self.target = target
        self.is_alive = True

    def make_move(self, move_counter, game_map):
        self.hunger_update(move_counter)

        if self.hungry == 100:
            return

        self.moves = game_map.get_moves(self._y, self._x, self.target)

        if self.speed >= len(self.moves):
            self.moves = [self.moves[0]]
        else:
            self.moves = self.moves[:: self.speed]

        ny, nx = self.moves.pop()

        if isinstance(game_map.get_cell(ny, nx), self.target):
            self.eat(game_map, ny, nx)
            self.y, self.x = ny, nx

        elif game_map.get_cell(ny, nx) is None:
            self.y, self.x = ny, nx

        else:
            self.moves = []

    def hunger_update(self, move_counter):
        if move_counter % 2 == 0:
            self.hungry -= 5

        if self.hungry == 0 or self.hungry < 0:
            self.is_alive = False

    def eat(self, ny, nx):
        if (100 - self.hungry) <= 50:
            self.hungry += 100 - self.hungry
        else:
            self.hungry += 50










