
# Класс карты, принимающий конфиг из высоты и толщины

class GameMap:

    def __init__(self, config):
        self.height = config["height"]
        self.width = config["weight"]
        self.grid = {i: [None] * self.width for i in range(self.height)}
        self.objects = []
        self.objects_count = {}

    def get_empty_cells(self) -> list:
        return [(y, x) for y in range(self.height) for x in range(self.width) if self.grid[y][x] == None]

    # Потенциальный костыль (Доделать)
    # def is_cell_empty(self, x, y):
    #     return self.

    def get_population(self, object_name) -> int:
        return self.population[object_name]

    def add_object(self, obj):
        self.objects.append(obj)
        if obj.__class__.__name__ not in self.objects_count:
            self.objects_count[obj.__class__.__name__] = 0
        self.population[obj.__class__.__name__] += 1

    def remove_object(self, obj):
        self.objects.remove(obj)
        self.population[obj.__class__.__name__] -= 1

    # Костыль удалить
    # def clear_cell(self, x: int, y: int):
    #     self.grid[y][x] = None

    def set_obj(self, x: int, y: int, obj):
        self.grid[y][x] = obj
