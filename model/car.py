class Car(object):
    """
    A class to store the floor position (floor) and the max capacity of a elevator
    """

    def __init__(self, floor=0, capacity=1, direction=1):
        self.floor = floor
        self.capacity = capacity
        self.direction = direction
        self.in_people = 0
        self.full = False

    @property
    def floor(self):
        return self.floor

    @floor.setter
    def floor(self, value):
        self.floor = value

    @property
    def capacity(self):
        return self.capacity

    @capacity.setter
    def capacity(self, value):
        self.capacity = value

    @property
    def direction(self):
        return self.direction

    @direction.setter
    def direction(self, value):
        self.direction = value

    @property
    def in_people_number(self):
        return self.in_people_number

    @in_people_number.setter
    def in_people_number(self, value):
        self.in_people_number = value

    @property
    def full(self):
        return self.full

    @full.setter
    def full(self, value):
        self.full = value
