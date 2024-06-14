import logging


class Car(object):
    """
    A class to store the floor position (floor) and the max capacity of a elevator
    """

    def __init__(
        self,
        id,
        no_floors,
        env,
        target_floor=0,
        current_floor=0,
        capacity=1,
        direction=0,
    ):
        self._id = id
        self._no_floors = no_floors
        self._current_floor = current_floor
        # self._target_floor = target_floor
        self._capacity = capacity
        self._no_movements = 0
        self._direction = direction
        self._in_people = 0
        self._env = env
        self._full = False

    @property
    def id(self):
        return self._id

    @property
    def current_floor(self):
        return self._current_floor

    @current_floor.setter
    def current_floor(self, value):
        self._current_floor = value

    # @property
    # def target_floor(self):
    #     return self._target_floor
    #
    # @target_floor.setter
    # def target_floor(self, value):
    #     self._target_floor = value

    @property
    def capacity(self):
        return self._capacity

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value

    @property
    def in_people(self):
        return self._in_people

    @in_people.setter
    def in_people(self, value):
        self._in_people = value

    @property
    def full(self):
        if self._in_people == self._capacity:
            self._full = True
        else:
            self._full = False
        return self._full

    def movement(self):
        self._current_floor += self._direction
        logging.info(
            f"Car {self._id} moves from {self._current_floor - self._direction} to {self._current_floor} at simulation step {self._env.now}"
        )
        self._no_movements += 1

    def __str__(self):
        return f"Car {self._id}: [current floor: {self._current_floor}, direction: {self._direction}, number of people: {self._in_people}, capacity: {self._capacity}, movements: {self._no_movements}]"
