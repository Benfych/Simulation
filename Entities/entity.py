from dataclasses import dataclass

# Изначальный класс, от которого наследуются все объекты
class Entity:

        def __init__(self, y: int, x:int):
                self.y = y
                self.x = x
                

        def update(self, *args, **kwargs):
                pass

    

    


        