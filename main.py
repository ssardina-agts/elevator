
from controller.baseline_agents import Baseline
from model.simulator import Simulator
import coloredlogs
import logging


def main():
    simulator = Simulator(people_number=2, floors_number=2, info_cars={"car_number": 1, "capacity": [1]})
    agent = Baseline()

    simulator.register_agent(agent)
    simulator.run()


if __name__ == "__main__":
    main()
