from .entity import Entity


class EmptyCell(Entity):
    def __init__(self, y, x):
        super().__init__(y, x)
