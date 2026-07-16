from actions import Action


class PopulationControl(Action):
    def __init__(self, game_map, spawner, spawner_config):
        self.game_map = game_map
        self.spawner = spawner
        self.spawn_config = spawner_config

    def run(self):
        for obj in self.spawn_config:
            if obj.count > self.game_map.get_population(obj.name):
                self.spawner.run(obj)
