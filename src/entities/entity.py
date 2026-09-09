class Entity:
    """
        Изначальный класс, от которого наследуются все объекты
        Хранит кординаты в декардовой системе кординат

        Attributes:
                x (int): кордината по осси x
                y (int): кордината по осси y
                self._to_remove (bool): флаг для удаления объекта

    """

    def __init__(self, cord):
        self.x = cord[0]
        self.y = cord[1]
        self._to_remove = False

    def remove_entity(self):
        self._to_remove = True
