

class Population_control:
    def __init__(self, map, spawner, simulation):
        self.map = map
        self.spawner = spawner
        self.simulation = simulation

    def run(self):
        for obj in self.simulation.spawn_config:
            if obj.count > self.map.get_population(obj.name):
                self.spawner.run(obj)                

    
