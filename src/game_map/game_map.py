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
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    def get_cell(self, y, x):
        return self._grid[y][x]


    def get_population(self, object_name) -> int:
        return self._population[object_name]

    def add_object(self, obj):
        self._objects.append(obj)
        self._population[obj.__class__.__name__] += 1

    def remove_object(self, obj):
        self._grid[obj.y][obj.x] = None
        self._objects.remove(obj)
        self._population[obj.__class__.__name__] -= 1

    def set_obj(self, x: int, y: int, obj):
        self._grid[y][x] = obj

    #
    # def get_empty_cells(self) -> list:
    #     return [
    #         (y, x)
    #         for y in range(self._height)
    #         for x in range(self._width)
    #         if self._grid[y][x] == None
    #     ]
