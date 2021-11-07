class Car(object):
    """
    A class to store the floor position (floor) and the max capacity of a elevator
    """

    def __init__(self, id, target_floor=0, current_floor=0, capacity=1, direction=0):
        self._id = id
        self._current_floor = current_floor
        self._target_floor = target_floor
        self._capacity = capacity
        self._direction = direction
        self._in_people = 0
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

    @property
    def target_floor(self):
        return self._target_floor

    @target_floor.setter
    def target_floor(self, value):
        self._target_floor = value

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
        if self._in_people < self._capacity:
            self._full = False
        return self._full

    def go(self, direction, target):
        self._direction = direction
        self._target_floor = target

    def stop(self):
        self._direction = 0
        self._target_floor = -1

    def __str__(self):
        return f"Car {self._id}: [{self._current_floor}, {self._direction}, {self._in_people}]"
