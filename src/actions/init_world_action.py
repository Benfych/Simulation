from actions import Action


class InitWorld(Action):
    def __init__(self, spawner, spawn_config):
        self.spawner = spawner
        self.spawn_config = spawn_config

    def run(self):
        for config in self.spawn_config:
            for _ in range(config.count):
                self.spawner.run(config)

