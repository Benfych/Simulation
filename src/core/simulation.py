from game_map import GameMap


class Simulation:

    def __init__(self):
        self.map = Map()

        self.spawner = Spawner(self.map)

        self.init_actions = [
            Init_world(self.map, self, self.spawner)
        ]

        self.turn_actions = [
            Map_update(self.map),
            Next_move(self.map, self),
            Render(self.map),
            Population_control(self.map, self.spawner, self)
        ]

        self._move_counter = 0

        self.spawn_config = [
            APPLE_DEFAULT_CONFIG,
            PREDATOR_DEFAULT_CONFIG,
            HERBIVORE_DEFAULT_CONFIG,
            TREE_DEFAULT_CONFIG,
            ROCK_DEFAULT_CONFIG
        ]

        self.FPS = 1 / 10
        self.start = time.time()

    def init_simulation(self):
        self.init_actions[0].run()

    def next_turn(self):
        while True:

            print(
                "(1): 1 ход\n",
                "(2): выход",
                sep=""
            )
            choice = input("Выбор: ")

            if choice == "1":
                os.system('cls')
                self.turn_actions[1].run()
                self.turn_actions[0].run()
                self.turn_actions[2].run()
                self.turn_actions[3].run()
                print(self._move_counter)

            if choice == "2":
                break

    def start_simulation(self):
        while True:
            os.system('cls')
            start = time.perf_counter()

            self.turn_actions[1].run()
            self.turn_actions[0].run()
            self.turn_actions[2].run()
            self.turn_actions[3].run()
            print(
                "Выход: ctrl + c"
            )

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
                sep=""
            )
            choice = input("Выбор: ")

            if choice == "1":
                self.init_actions[0].run()
                self.start_simulation()

            elif choice == "2":
                self.init_actions[0].run()
                self.turn_actions[1].run()
                self.turn_actions[0].run()
                self.turn_actions[2].run()
                self.next_turn()

            elif choice == "3":
                break

