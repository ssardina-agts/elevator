class State(object):
    """
    A simple class to store the state of the system
    """

    def __init__(self, cars, people, no_floors, no_people, no_cars, id):

        self._cars = cars
        self._people = people
        self._no_floors = no_floors
        self._no_people = no_people
        self._no_cars = no_cars
        self._all_people_arrive = False
        self._id_sim = id

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
    def no_floors(self):
        return self._no_floors

    @property
    def no_people(self):
        return self._no_people

    @property
    def no_cars(self):
        return self._no_cars

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

        return f"""
            Id simulation: {self._id_sim}
            {people_str}
            {cars_str}
            """
