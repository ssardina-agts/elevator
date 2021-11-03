from model.person import Person
from model.car import Car


class State(object):
    """
    A simple class to store the state of the system
    """

    def __init__(self, people_number, floors_number, info_cars):
        people = []
        cars = []
        self._people_number=people_number
        self._floors_number = floors_number
        self._floor_population = [0] * (self.floors_number)
        for idx in range(self._people_number):
            person = Person(floors_number=self._floors_number)
            # s_f = person.start_floor  # s_f is shorthand for start_floor to clean the code

            # floor_population[s_f] += 1
            people.append(person)
        for idx in range(info_cars['car_number']):
            car = Car(capacity_value=info_cars['capacity'][idx])
            cars.append(car)

        self._status = {"people": people, "cars": cars, "floors_number": self._floors_number, 'arrived_people_number': 0}

    @property
    def status(self):
        return self._status


    @property
    def wait_times(self):
        self._wait_times = []
        for person in self._status['people']:
            if not person.arrived:
                print('Somethings gone wrong')
            self._wait_times.append(person.wait_time)
        return self._wait_times

    @property
    def people_number(self):
        return self._people_number

    @property
    def floors_number(self):
        return self._floors_number

    @property
    def floor_population(self):
        return self._floor_population

    @floor_population.setter
    def floor_population(self, value):
        self._floor_population = value



    def print(self):
        print('\nstatus')
        idx=0
        for person in self._status['people']:
            print('\nperson '+str(idx))
            person.print()
            idx+=1
        idx = 0
        for car in self._status['cars']:
            print('\ncar ' + str(idx))
            car.print()
            idx += 1
