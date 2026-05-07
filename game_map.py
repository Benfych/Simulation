from cfg.herbivore_cfg import *



# Класс карты, принимающий конфиг из высоты и толщины

class Map:

    def __init__(self, height: int, width: int, patchfinder):
        self.height: int = height
        self.width: int = width
        self.grid = {i: [None] * self.width for i in range(self.height)}
        self.pathfinding = patchfinder(self)
        self.objects = []
        self.population = {
            "Apple": 0,
            "Predator": 0,
            "Herbivore": 0,
            "Rock": 0,
            "Tree": 0
        }
        

    def get_empty_cells(self) -> list:
        return [(y, x) for y in range(self.height) for x in range(self.width) if self.grid[y][x] == None]
    
    def get_population(self, object_name) -> int:
        return self.population[object_name]

    def add_object(self, obj):
        self.objects.append(obj)
        self.population[obj.__class__.__name__] += 1

    def remove_object(self, obj):
        self.objects.remove(obj)
        self.population[obj.__class__.__name__] -= 1
        
    def clear_cell(self, x:int, y:int):
        self.grid[y][x] = None
    
    def set_obj(self, x:int, y:int, obj):
        self.grid[y][x] = obj


        
    



        
        