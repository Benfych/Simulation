from dataclasses import dataclass
from actions.action import Action
from game_map import Map



class Render(Action):
    def __init__(self, map: Map):
        self.map = map

    def run(self):
        print("---------------------------------------------------------------")
        for y in range(self.map.height - 1):
                print("| " + " ".join(" ·" if x is None else str(x) for x in self.map.grid[y]) + " |")
        print(f"🐰: {self.map.population["Herbivore"]}  🐺: {self.map.population["Predator"]}  🍎: {self.map.population["Apple"]}  ------------------------------------------\n")
