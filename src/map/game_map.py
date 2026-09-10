
# Класс карты, принимающий конфиг из высоты и толщины

class GameMap:

    def __init__(self, config):
        self._height = config["height"]
        self._width = config["weight"]
        self._grid = {i: [None] * self.width for i in range(self.height)}
        self._objects = []
        self._objects_count = {}

    # Нахрен нужен костыль
    # def get_empty_cells(self) -> list:
    #     return [(y, x) for y in range(self.height) for x in range(self.width) if self.grid[y][x] == None]

    def get_population(self, object_name) -> int:
        return self._objects_count[object_name]

    def add_object(self, obj):
        self._objects.append(obj)
        if obj.__class__.__name__ not in self.objects_count:
            self._objects_count[obj.__class__.__name__] = 0
        self._objects_count[obj.__class__.__name__] += 1

    def remove_object(self, obj):
        self._objects.remove(obj)
        self._objects_count[obj.__class__.__name__] -= 1

    def set_obj(self, cord):
        self.grid[cord["x"]][cord["y"]] = obj

    def get_height(self):
        return self._height

    def get_width(self):
        return self._width

    def is_free(self, x, y):
