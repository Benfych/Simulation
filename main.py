from src.conf import MAP_CONF
from src.core import Simulation
from src.game_map import GameMap
from src.pathfinding import PathfinderBFS
from src.render import CLIRender

game_map = GameMap(MAP_CONF)
pathfinder = PathfinderBFS(game_map)
render = CLIRender(game_map)
simulation = Simulation(game_map, render, pathfinder)

def main():
    try:
        while True:
            print(
                "(1): запустить бесконечную симуляцию\n",
                "(2): 1 ход\n",
                "(3): выход",
                sep=""
            )
            choice = input("Выбор: ")

            if choice == "1":
                simulation.start_simulation()

            elif choice == "2":
                simulation.next_turn()

            elif choice == "3":
                simulation.clear_CLI()
                exit()

    except KeyboardInterrupt:
        main()


if __name__ == '__main__':
    main()
