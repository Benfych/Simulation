from simulation import Simulation

if __name__ == "__main__":
    try:
        a = Simulation()
        a.interface()
    except KeyboardInterrupt:
        print("Симуляция прекращена")
