import random
import logging


class Person(object):
    """
    This is an object used to model each person in the simulation. Each person has various attributes
    """

    population = 0  # This keeps track of how many people have been generated

    def __init__(self, id, no_floors, env):

        self._id = id

        # set randomly the current and target floors (excluding the case when both are equals)
        self._current_floor = random.randint(0, no_floors - 1)
        self._target_floor = random.randint(0, no_floors - 1)
        while self._current_floor == self._target_floor:
            self._target_floor = random.randint(0, no_floors - 1)
        self._direction = 1 if self._current_floor < self._target_floor else -1
        self._in_car = False
        self._id_car = None
        self._arrived = False
        self._wait_time = 0
        self._env = env

    @property
    def id(self):
        return self._id

    @property
    def current_floor(self):
        return self._current_floor

    @current_floor.setter
    def current_floor(self, value):
        self._current_floor = value

    @property
    def target_floor(self):
        return self._target_floor

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value

    @property
    def in_car(self):
        return self._in_car

    @in_car.setter
    def in_car(self, value):
        self._in_car = value

    @property
    def id_car(self):
        return self._id_car

    @id_car.setter
    def id_car(self, value):
        self._id_car = value

    @property
    def arrived(self):
        return self._arrived

    @property
    def wait_time(self):
        return self._wait_time

    @property
    def env(self):
        return self._env

    def __str__(self):
        return (
            f"Person {self._id}: [current floor: {self._current_floor}, target floor: {self._target_floor}"
            f", id car: {self._id_car}, arrived: {self._arrived}, total steps to get goal: {self._wait_time}]"
        )

    def arriving(self, cars):
        # process when a person arrives
        if self._in_car and self._current_floor == self._target_floor:
            self._arrived = True
            self._wait_time = self._env.now
            cars[self._id_car].in_people -= 1
            self._in_car = False
            logging.info(
                f"Person {self._id} arrives on floor {self._current_floor} at simulation step {self._env.now}"
            )

    def getting_in(self, cars):
        # locking for a available car
        if not self._in_car and not self._arrived:
            for car in cars:
                if (
                    car.current_floor == self._current_floor
                    and not car.full
                    and self._direction == car.direction
                    and not self._in_car
                ):
                    self._in_car = True
                    self._id_car = car.id
                    car.in_people += 1
                    logging.info(
                        f"Person {self._id} gets in car {self._id_car} in floor {self._current_floor} at simulation step {self._env.now}"
                    )
