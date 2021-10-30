class Car(object):
    """
    A class to store the floor position (floor) and the max capacity of a elevator
    """

    def __init__(self, floor_value=0, capacity_value=1, direction_value=0):
        self._floor = floor_value
        self._capacity = capacity_value
        self._direction = direction_value
        self._in_people = 0
        self._full = False

    @property
    def floor(self):
        return self._floor

    @floor.setter
    def floor(self, value):
        self._floor = value

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        self._capacity = value

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


    def print(self):
        print('current floor: ', self._floor)
        print('direction_value: ', self._direction)
        print('people number in car: ', self._in_people)
