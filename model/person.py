import random


class Person(object):
    """
    This is an object used to model each person in the simulation. Each person has various attributes
    """
    population = 0  # This keeps track of how many people have been generated

    def __init__(self, id, floors_number):
        self.animation = None  # this stores the canvas object for each person
        # self.id = Person.population
        # Person.population += 1

        self.id = id

        self.elevator_spot = False
        self.current_floor = random.randint(0, floors_number - 1)
        self.target_floor = random.randint(0, floors_number - 1)
        while self.current_floor == self.target_floor:
            self.target_floor = random.randint(0, floors_number - 1)
        self.direction = (1 if self.current_floor < self.target_floor else -1)
        # self.distance = floorheight * (self.start_floor - self.target_floor)
        self.arrived = False
        self.in_car = False
        self.wait_time = 0

    def __str__(self):
        return f"Pearson {self.id}: [{self.current_floor}, {self.target_floor}, {self.in_car}, {self.arrived}]"

    # def arrived(self, floor):
    #     """Returns true if the person has arrived at where they wanted to go"""
    #     return True if floor == self.target_floor else False

    # def waiting(self):
    #     """
    #     Returns True if the person is not in the elevator, and they have not got where they are going
    #     :return: boolean of whether or not the person is waiting for the lift
    #     """
    #     return not self.in_car and not self.arrived
