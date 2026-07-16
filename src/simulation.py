# Логика
# ----------------------------------------
from game_map import GameMap
import time
import os

# -----------------------------------------


# Конфиги
# ----------------------------------------

from cfg.config import MAP_DEFAULT_CONFIG
from cfg.config import HERBIVORE_DEFAULT_CONFIG
from cfg.config import PREDATOR_DEFAULT_CONFIG
from cfg.config import APPLE_DEFAULT_CONFIG
from cfg.config import TREE_DEFAULT_CONFIG
from cfg.config import ROCK_DEFAULT_CONFIG

# -----------------------------------------

# Действия
# ----------------------------------------

from actions.init_world_action import InitWorld
from actions.next_move_action import Next_move
from actions.map_update_action import Map_update
from actions.render_action import Render
from actions.spawn_action import Spawner
from actions.population_control_action import PopulationControl

# -----------------------------------------


class Simulation:

    def __init__(self):
        self._move_counter = 0

        self.game_map = GameMap(
            MAP_DEFAULT_CONFIG.height,
            MAP_DEFAULT_CONFIG.width,
            MAP_DEFAULT_CONFIG.pathfinder,
        )

        self.spawner = Spawner(self.game_map)

        self.spawn_config = [
            APPLE_DEFAULT_CONFIG,
            PREDATOR_DEFAULT_CONFIG,
            HERBIVORE_DEFAULT_CONFIG,
            TREE_DEFAULT_CONFIG,
            ROCK_DEFAULT_CONFIG,
        ]

        self.init_actions = [InitWorld(self.spawner, self.spawn_config)]

        self.turn_actions = [
            Map_update(self.game_map),
            Next_move(self.game_map, self),
            Render(self.game_map, self),
            PopulationControl(self.game_map, self.spawner, self.spawn_config),
        ]

        self.FPS = 1 / 5
        self.start = time.time()

    @property
    def get_move_counter(self) -> int:
        return self._move_counter

    def move_counter_increment(self):
        self._move_counter += 1

    def init_simulation(self):
        self.init_actions[0].run()

    def next_turn(self):
        while True:

            print("(1): 1 ход\n", "(2): выход", sep="")
            choice = input("Выбор: ")

            if choice == "1":
                # os.system('cls')
                self.turn_actions[1].run()
                self.turn_actions[0].run()
                self.turn_actions[2].run()
                self.turn_actions[3].run()

            if choice == "2":
                break

    def start_simulation(self):
        while True:
            os.system("cls")
            start = time.perf_counter()

            self.turn_actions[1].run()
            self.turn_actions[0].run()
            self.turn_actions[2].run()
            self.turn_actions[3].run()

            print("Выход: ctrl + c")

            elapsed = time.perf_counter() - start
            sleep_time = 0.2 - elapsed

            if sleep_time > 0:
                time.sleep(sleep_time)

    def interface(self):
        while True:
            print(
                "(1): запустить бесконечную симуляцию\n",
                "(2): 1 ход\n",
                "(3): выход",
                sep="",
            )
            choice = input("Выбор: ")

            if choice == "1":
                self.init_actions[0].run()
                self.start_simulation()

            elif choice == "2":
                self.turn_actions[1].run()
                self.turn_actions[0].run()
                self.turn_actions[2].run()
                self.turn_actions[3].run()
                self.next_turn()

            elif choice == "3":
                break
