from controller.baseline_agents import Baseline, Efficient
from model.simulator import Simulator
import coloredlogs
import logging


def main():
    simulator = Simulator(people_number=10, floors_number=4, info_cars={"car_number": 1, "capacity": [1]})
    agent = Baseline()
    # agent = Efficient()

    simulator.register_agent(agent)
    simulator.run(animation_speed=0.5)


if __name__ == "__main__":
    main()
