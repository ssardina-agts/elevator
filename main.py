
from controller.agent import Baseline, RandomSlowAgent
from model.simulator import Simulator
import coloredlogs
import logging


def main():
    simulator = Simulator(num_steps=25, max_timestep_wait=2)
    agent = RandomSlowAgent(max_processing_time=1, throw_error=True, infinite_loop=True)

    simulator.register_agent(agent)
    simulator.run()


if __name__ == "__main__":
    main()
