from actions import Action


class Render(Action):
    def __init__(self, game_map, simulation):
        self.game_map = game_map
        self.simulation = simulation

    # def run(self):
    #     render()

    def render(self, move_counter):
        SPRITES_EMOJI = {
            "Herbivore": "🐰",
            "Apple": "🍎",
            "Tree": "🌳",
            "Rock": "🗿",
            "Predator": "🐺",
        }

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
        print(
            f"🐰: {self.get_population('Herbivore')}  🐺: {self.get_population('Predator')}  🍎: {self.get_population('Apple')}  ------------------------------------------\n"
        )
