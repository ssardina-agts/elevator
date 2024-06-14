from controller.agent import Agent
from random import random
import logging


class Baseline(Agent):

    def __init__(self):
        super().__init__("Baseline")

    def next_actions(self):
        """
        This is a baseline agent that controls the cars with a simple system. A car go from the lowest floor to the highest floor
        and vice-versa.
        Possible actions: 1(up), -1(down), and 0(stop)
        """
        actions = []
        for car in self.state.cars:
            if car.current_floor == 0:
                actions.append(1)
            elif car.current_floor == self.state.no_floors - 1:
                actions.append(-1)
            else:
                actions.append(car.direction)
        return actions


class Random(Agent):

    def __init__(self, probability=0.5):
        super().__init__("Random")
        self._prob = probability

    def next_actions(self):
        """
        This is a baseline agent that controls the cars with a simple system. A car go from the lowest floor to the highest floor
        and vice-versa.
        Possible actions: 1(up), -1(down), and 0(stop)
        """
        actions = []
        for car in self.state.cars:
            if random() > self._prob:
                if car.current_floor == self.state.no_floors - 1:
                    actions.append(0)
                else:
                    actions.append(1)
            else:
                if car.current_floor == 0:
                    actions.append(0)
                else:
                    actions.append(-1)
        return actions
