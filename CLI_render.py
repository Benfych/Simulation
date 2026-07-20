class Render:
    SPRITES_EMOJI = {
        "Herbivore": "🐰",
        "Apple": "🍎",
        "Tree": "🌳",
        "Rock": "🗿",
        "Predator": "🐺",
    }

    def __init__(self, game_map):
        self._game_map = game_map

    def render(self, move_counter):
        print(f"Номер хода: {move_counter}")
        print("---------------------------------------------------------------")
        for y in range(self._height):
            print(
                "| "
                + " ".join(
                    " ·" if x is None else SPRITES_EMOJI[x.__name__]
                    for x in self._grid[y]
                )
                + " |"
            )

        herbivore_population = self._game_map.herbivore_population


        print(
            f"🐰: {self._game_map.get_population('Herbivore')}  🐺: {self.get_population('Predator')}  🍎: {self.get_population('Apple')}  ------------------------------------------\n"
        )
