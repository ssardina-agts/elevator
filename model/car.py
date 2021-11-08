class Car(object):
    """
    A class to store the floor position (floor) and the max capacity of a elevator
    """

    def __init__(self, id, max_floor, target_floor=0, current_floor=0, capacity=1, direction=0):
        self._id = id
        self._max_floor = max_floor
        self._current_floor = current_floor
        self._target_floor = target_floor
        self._capacity = capacity
        self._direction = direction
        self._in_people = 0
        self._door_open = False
        self._floors_buttons = []
        self._full = False

    @property
    def id(self):
        return self._id

    @property
    def current_floor(self):
        return self._current_floor

    @property
    def door_open(self):
        return self._door_open

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
        self._current_floor = max(0, min(self._current_floor + self._direction, self._max_floor))

    def stop(self):
        self._direction = 0
        self._target_floor = -1


    @property
    def floors_buttons(self):
        return self._floors_buttons

    def push_floor_button(self, n):
        self._floors_buttons.append(n)

    def flush_floors_buttons(self):
        self._floors_buttons = []


    def __str__(self):
        return f"Car {self._id}: [floor({self._current_floor}), door({self.door_open}), dir({self._direction}), people({self._in_people}), buttons({self.floors_buttons})]"
