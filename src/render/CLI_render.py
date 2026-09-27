class CLIRender:
    """
    Консольный рендер карты.

    Отвечает за визуализацию состояния GameMap в терминале:
    выводит сетку с символами объектов и легенду с количеством
    существ каждого типа.

    Attributes:
        _game_map (GameMap): карта для отрисовки.
        CREATURES_SPRITES (dict[str, str]): маппинг имени класса
    """


    def __init__(self, game_map):
        self._game_map = game_map

    CREATURES_SPRITES = {
        "Herbivore": "🐰",
        "Apple": "🍎",
        "Tree": "🌳",
        "Rock": "🗿",
        "Predator": "🐺",
    }

    def render(self, move_counter):
        print("-" * (3 * self._game_map.get_width() + 3))
        for y in range(self._game_map.get_height() - 1):
            print("| " + " ".join(". " if self._game_map.get_object(x, y) is None
                                  else self.CREATURES_SPRITES[self._game_map.get_object(x, y).__class__.__name__]
                                  for x in range(self._game_map.get_width())) + " |"
                  )

        print("-" * (3 * self._game_map.get_width() + 3))
        print(
            f"{self.CREATURES_SPRITES['Herbivore']}: {self._game_map.get_objects_count('Herbivore')}  "
            f"{self.CREATURES_SPRITES['Predator']}: {self._game_map.get_objects_count('Predator')}  "
            f"{self.CREATURES_SPRITES['Apple']}: {self._game_map.get_objects_count('Apple')}\n"
        )

        print("Пауза: ctrl + c")
