from actions import Action


class NextMove(Action):
    def __init__(self, game_map, simulation):
        self.game_map = game_map
        self.simulation = simulation

    def run(self):
        self.simulation.move_counter_increment()
        self.game_map.next_move_objects(self.simulation.get_move_counter)

    # def cleaner(self):
    #     if
