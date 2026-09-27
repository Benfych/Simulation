import os
import time

from ..actions.init import InitWorldAction
from ..actions.tick import NextMoveAction, EntityRemoverAction, EntitiesRespawnAction


class Simulation:

    def __init__(self, game_map, render, pathfinder):
        self.frame_time = 1 / 10
        self._sim_move_counter = 0
        self._world_init = 0
        self._game_map = game_map
        self._pathfinder = pathfinder
        self._render = render
        self._init_actions = [InitWorldAction(self._game_map)]
        self._tick_actions = [NextMoveAction(self._game_map, self._pathfinder),
                              EntityRemoverAction(self._game_map, self._pathfinder),
                              EntitiesRespawnAction(self._game_map)]

    def clear_CLI(self):
        os.system("cls" if os.name == "nt" else "clear")

    def next_turn(self):
        self.clear_CLI()
        if self._world_init != 1:
            self._init_actions[0].execute()
            self._world_init = 1
        self._sim_move_counter += 1l
        self._render.render(self._sim_move_counter)
        for action in self._tick_actions:
            action.execute()

    def start_simulation(self):
        self._sim_move_counter += 1
        while True:
            self.clear_CLI()
            start = time.perf_counter()

            if self._world_init != 1:
                self._init_actions[0].execute()
                self._world_init = 1

            self._render.render(self._sim_move_counter)
            for action in self._tick_actions:
                action.execute()
            elapsed = time.perf_counter() - start
            sleep_time = self.frame_time - elapsed

            if sleep_time > 0:
                time.sleep(sleep_time)

    def pause_simulation(self):

        print("(1) Продолжить")
        print("(2) Выйти")
