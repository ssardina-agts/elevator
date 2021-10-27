from model.state import State
from controller.agent import Agent


class Simulator(object):

    def __init__(self, people_number=5, floor_number=4, cars=None):
        if cars is None:
            cars = {"car_number": [1], "capacity": [1] }

        self._state = State(people_number,floor_number,cars)
        self._all_done = False
        self._agent = None

    def register_agent(self, agent: Agent):
        self._agent = agent
