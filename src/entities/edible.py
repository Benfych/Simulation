from .entity import Entity

class Edible():
        """
        Класс, от которого дополнительно наследуются съедобные объекты
        Attr:
            - nutrition (int): пищевая ценность объекта
            отвечает за количество восполняемогго голода

        """

        def __init__(self, nutrition):
            self._nutrition = nutrition

        def on_eat(self):
            self.to_remove()
            return self._nutrition


