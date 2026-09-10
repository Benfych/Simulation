

class CLI_render:
    CREATURES_SPRITES = {
        "Herbivore": "🐰",
        "Apple": "🍎",
        "Tree": "🌳",
        "Rock": "🗿",
        "Predator": "🐺",
    }

    def render(self, move_counter):
        print("---------------------------------------------------------------")
        for y in range(self.map.height - 1):
            print("| " + " ".join(
                " ·" if x is None else creature_sprites[x.__class__.__name__] for x in self.map.grid[y]) + " |")
        print(
            f"{creature_sprites['herbivore']}: {self.map.population['Herbivore']}  "
            f"{creature_sprites['predator']}: {self.map.population['Predator']}  "
            f"{creature_sprites['apple']}: {self.map.population['Apple']}  "
            "------------------------------------------\n"
        )
