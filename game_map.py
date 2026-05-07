from cfg.herbivore_cfg import *

class Map:
    def __init__(self, height: int, width: int, patchfinder):
        self._height: int = height
        self._width: int = width
        self._grid = {i: [None] * self._width for i in range(self._height)}
        self._pathfinding = patchfinder(self)
        self._objects = []
        self._population = {
            "Apple": 0,
            "Predator": 0,
            "Herbivore": 0,
            "Rock": 0,
            "Tree": 0
        }
        
    @property
    def get_width(self) -> int:
        return self._width

    @property
    def get_height(self) -> int:
        return self._height

    @property
    def get_objects(self) -> list:
        return self._objects

    @property
    def get_grid(self) -> dict:
        return self._grid

    def get_empty_cells(self) -> list:
        return [(y, x) for y in range(self._height) for x in range(self._width) if self._grid[y][x] == None]

    def get_population(self, object_name) -> int:
        return self._population[object_name]

    def add_object(self, obj):
        self._objects.append(obj)
        self._population[obj.__class__.__name__] += 1

    def remove_object(self, obj):
        self._objects.remove(obj)
        self._population[obj.__class__.__name__] -= 1
        
    def clear_cell(self, x:int, y:int):
        self._grid[y][x] = None
    
    def set_obj(self, x:int, y:int, obj):
        self._grid[y][x] = obj



        