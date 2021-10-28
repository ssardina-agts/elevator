from model.person import Person
from model.car import Car


class State(object):
    """
    A simple class to store the state of the system
    """

    def __init__(self, people_number, floors_number, info_cars):
        people = []
        cars = []
        for idx in range(people_number):
            person = Person(floors_number=floors_number)
            # s_f = person.start_floor  # s_f is shorthand for start_floor to clean the code

            # floor_population[s_f] += 1
            people.append(person)
        for idx in range(info_cars['car_number']):
            car = Car(capacity_value=info_cars['capacity'][idx])
            cars.append(car)

        self._status = {"people": people, "cars": cars, "floors_number": floors_number, 'arrived_people_number': 0}

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value: dict):
        self._status = value
