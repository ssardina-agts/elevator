from model.person import Person
from model.car import Car


class State(object):
    """
    A simple class to store the state of the system
    """

    def __init__(self, people_number, floors_number, cars_info):
        self._people_number=people_number
        self._floors_number = floors_number
        self._floor_population = [0] * (self.num_floors)

        self._people = []
        for idx in range(self._people_number):
            person = Person(floors_number=self._floors_number)
            # s_f = person.start_floor  # s_f is shorthand for start_floor to clean the code

            # floor_population[s_f] += 1
            self._people.append(person)

        self._cars = []
        for idx in range(len(cars_info)):
            self._cars.append(Car(id=idx, capacity=cars_info[idx]))

        # self._status = {"people": people, "cars": cars, "floors_number": self._floors_number, 'arrived_people_number': 0}

        self._arrived_people_number = 0

    # @property
    # def status(self):
    #     # return self._status
    #     return {"people": self._people, "cars": self._cars, "floors_number": self._floors_number, 'arrived_people_number': self._arrived_people_number}

    @property
    def people(self):
        return self._people

    @property
    def cars(self):
        return self._cars

    @property
    def num_arrived(self):
        return self._arrived_people_number

    @num_arrived.setter
    def num_arrived(self, value):
        self._arrived_people_number = value


    @property
    def wait_times(self):
        self._wait_times = []
        for person in self.people:
            if not person.arrived:
                print('Somethings gone wrong')
            self._wait_times.append(person.wait_time)
        return self._wait_times

    @property
    def num_people(self):
        return self._people_number

    @property
    def num_floors(self):
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
        for person in self._people:
            print('\nperson '+str(idx))
            person.print()
            idx+=1
        idx = 0
        for car in self._cars:
            print('\ncar ' + str(idx))
            car.print()
            idx += 1
