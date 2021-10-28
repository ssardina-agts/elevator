
import asyncio
from abc import ABC, abstractmethod

from model.state import State


class Agent(ABC):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # @abstractmethod
    # def initialised(self, state: State):
    #     """
    #     Called when the simulator is initialised.
    #     :type state: Initial state of the system.
    #     :return:
    #     """
    #     raise NotImplementedError()

    @abstractmethod
    def next_actions(self, state: State) -> dict:
        """
        Called when simulator is ready to take the next action
        :type state: An object of the system state.
        :param time_step: time step for which action is requested.
        :return:
        """
        raise NotImplementedError()




