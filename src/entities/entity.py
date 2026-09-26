class Entity:
    """
        Изначальный класс, от которого наследуются все объекты
        Хранит кординаты в декардовой системе кординат

        Attributes:
                x (int): кордината по осси x
                y (int): кордината по осси y
                self._to_remove (bool): флаг для удаления объекта
                nutritional (int): энергетическая ценность, 0 по умолчаниб
    """

    def __init__(self, y, x):
        self._y = y
        self._x = x
        self._to_remove = False

    def to_remove(self):
        self._to_remove = True

    def get_remove_status(self):
        return self._to_remove

    def get_cords(self):
        return self._y, self._x
