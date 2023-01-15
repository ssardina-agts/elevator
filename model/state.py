class State(object):
    """
    A simple class to store the state of the system
    """

    def __init__(self, cars, people, num_floors, num_people,num_cars):

        self._cars = cars
        self._people = people
        self._num_floors = num_floors
        self._num_people = num_people
        self._num_cars=num_cars
        self._all_people_arrive = False

    @property
    def cars(self):
        return self._cars

    @cars.setter
    def cars(self, value):
        self._cars = value

    @property
    def people(self):
        return self._people

    @people.setter
    def people(self, value):
        self._people = value

    @property
    def num_floors(self):
        return self._num_floors

    @property
    def num_people(self):
        return self._num_people

    @property
    def num_cars(self):
        return self._num_cars

    @property
    def all_people_arrive(self):
        return self._all_people_arrive

    @all_people_arrive.setter
    def all_people_arrive(self, boolean):
        self._all_people_arrive = boolean

    def __str__(self):
        people_str = ""
        for person in self._people:
            people_str += "\t" + str(person) + "\n"

        cars_str = ""
        for car in self._cars:
            cars_str += "\t" + str(car) + "\n"

        return "\n" + people_str + "\n" + cars_str
