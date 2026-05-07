from dataclasses import dataclass
from actions.action import Action
from game_map import Map



class Render(Action):
    def __init__(self, map: Map):
        self.map = map
    def run(self):
        print("---------------------------------------------------------------")
        for y in range(self.map.get_height - 1):
                print("| " + " ".join(" ·" if x is None else str(x) for x in self.map.get_grid[y]) + " |")
        print(f"🐰: {self.map.get_population("Herbivore")}  🐺: {self.map.get_population("Predator")}  🍎: {self.map.get_population("Apple")}  ------------------------------------------\n")
