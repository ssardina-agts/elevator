from model.person import Person
from model.car import Car


class State(object):
    """
    A simple class to store the state of the system
    """

    def __init__(self, people_number, floors_number, info_cars):
        people = []
        cars = []
        cars_empty = True
        all_people_arrived = False
        for idx in range(people_number):
            person = Person(floors_number)
            # s_f = person.start_floor  # s_f is shorthand for start_floor to clean the code

            # floor_population[s_f] += 1
            people.append(person)
        for idx in range(len(info_cars['car_number'])):
            car = Car(capacity=info_cars['capacity'][idx])
            cars.append(car)

        self.status = {"people": people, "cars": cars, "floors_number": floors_number, 'cars_empty': cars_empty,
                       'all_people_arrived': all_people_arrived}

    @property
    def status(self):
        return self.status

    @status.setter
    def status(self, value: dict):
        self.status = value
