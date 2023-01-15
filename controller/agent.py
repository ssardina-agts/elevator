import logging
from abc import ABC, abstractmethod


class Agent(ABC):

    def __init__(self, name, state=None):
        self._name = name
        self._state = state

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @abstractmethod
    def next_actions(self) -> list:
        """
        Called when simulator is ready to take the next action
        :type state: An object of the system state.
        :param time_step: time step for which action is requested.
        :return:
        """
        raise NotImplementedError()

