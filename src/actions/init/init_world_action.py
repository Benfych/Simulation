from actions.action import Action
from dataclasses import dataclass
from actions.spawn_action import Spawner

class Init_world(Action):

    def __init__(self, map, simulation, spawner):
        self.map = map
        self.simulation = simulation
        self.spawner = spawner

    def run(self):
        for config in self.simulation.spawn_config:
            for _ in range(config.count):
                self.spawner.run(config)                



    