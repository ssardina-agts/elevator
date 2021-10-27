from model.person import Person
from model.car import Car

class State(object):
    """
    A simple class to store the state of the system
    """

    def __init__(self,number_of_people,number_of_floors,cars):
        for idx in range(number_of_people):
            person = Person(number_of_floors)
            s_f = person.start_floor  # s_f is shorthand for start_floor to clean the code

            floor_population[s_f] += 1
            total_population.append(person)
        elevator_direction = 1

        self._status = 0

    @property
    def elevator_floor(self):
        return self._elevator_floor

    @elevator_floor.setter
    def elevator_floor(self, value):
        self._elevator_floor = value
