from cfg.herbivore_cfg import *
from entities import Creature


class GameMap:
    def __init__(self, height: int, width: int, pathfinder):
        self._height: int = height
        self._width: int = width
        self._grid = {i: [None] * self._width for i in range(self._height)}
        self.reservation_cell = set()
        self._objects = []
        self.pathfinder = pathfinder(self)
        self._population = {
            "Apple": 0,
            "Predator": 0,
            "Herbivore": 0,
            "Rock": 0,
            "Tree": 0,
        }

    @property
    def get_width(self) -> int:
        return self._width

    @property
    def get_height(self) -> int:
        return self._height

    @property
    def get_grid(self) -> dict:
        return self._grid.copy()

    def get_cell(self, y, x):
        return self._grid[y][x]

    def get_moves(self, y, x, target) -> list:
        return self.pathfinder.get_moves(y, x, target)

    def clear_map(self):
        self._grid = {i: [None] * self._width for i in range(self._height)}

    def get_empty_cells(self) -> list:
        return [
            (y, x)
            for y in range(self._height)
            for x in range(self._width)
            if self._grid[y][x] == None
        ]

    def clear_cell(self, y: int, x: int):
        self._grid[y][x] = None

    def get_population(self, object_name) -> int:
        return self._population[object_name]

    def add_object(self, obj):
        self._objects.append(obj)
        self._population[obj.__class__.__name__] += 1

    def remove_object(self, obj):
        self._objects.remove(obj)
        self.clear_cell(obj.y, obj.x)
        self._population[obj.__class__.__name__] -= 1

    def set_obj(self, x: int, y: int, obj):
        self.clear_cell(y, x)
        self._grid[y][x] = obj

    def next_move_objects(self, move_counter):
        self.reservation_cell = set()
        is_creature = lambda obj: isinstance(obj, Creature)
        for obj in filter(is_creature, self._objects):
            obj.next_move(self, move_counter)

    def map_update(self):
        self.clear_map()
        for obj in self._objects:
            self.set_obj(obj.x, obj.y, obj)

    def render(self, move_counter):
        SPRITES_EMOJI = {
            "Herbivore": "🐰",
            "Apple": "🍎",
            "Tree": "🌳",
            "Rock": "🗿",
            "Predator": "🐺",
        }

        print(f"Номер хода: {move_counter}")
        print("---------------------------------------------------------------")
        for y in range(self._height):
            print(
                "| "
                + " ".join(
                    " ·" if x is None else SPRITES_EMOJI[x.__name__]
                    for x in self._grid[y]
                )
                + " |"
            )
        print(
            f"🐰: {self.get_population('Herbivore')}  🐺: {self.get_population('Predator')}  🍎: {self.get_population('Apple')}  ------------------------------------------\n"
        )
