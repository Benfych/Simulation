# Класс карты, принимающий конфиг из высоты и толщины

class GameMap:

    def __init__(self, conf):
        self._height = conf["height"]
        self._width = conf["width"]
        self._grid = {y: [None] * self._width for y in range(self._height)}
        self._objects = []
        self._objects_count = {}

    def get_objects_count(self, object_name):
        return self._objects_count[object_name]

    def get_objects(self):
        return list(self._objects)

    def get_object(self, y, x):
        return self._grid[y][x]

    def add_object(self, obj):
        y, x = obj.get_cords()
        self._objects.append(obj)
        self._grid[y][x] = obj

        if obj.__class__.__name__ not in self._objects_count:
            self._objects_count[obj.__class__.__name__] = 0
        self._objects_count[obj.__class__.__name__] += 1

    def move_object(self, old_y, old_x, new_y, new_x, obj):
        self._grid[old_y][old_x] = None
        self._grid[new_y][new_x] = obj

    def remove_object(self, obj):
        y, x = obj.get_cords()
        self._objects.remove(obj)
        self._grid[y][x] = None

        if self._objects_count[obj.__class__.__name__] > 0:
            self._objects_count[obj.__class__.__name__] -= 1
        else:
            del self._objects_count[obj.__class__.__name__]

    def get_height(self):
        return self._height

    def get_width(self):
        return self._width

    def is_free(self, y, x):
        if self._grid[y][x] is None:
            return True
        else:
            return False

    def is_valid(self, y, x, obj):
        """
        Функция для сравнения объекта с клеткой на карте

        """
        if  (0 <= x < self._width and 0 <= y < self._height):
            if isinstance(self._grid[y][x], obj):
                return True
            else:
                return False
        else:
            return False
