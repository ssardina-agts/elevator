from model.state import State
from controller.agent import Agent
from view.screen import Screen

import logging
import simpy
from model.car import Car
from model.person import Person


class Simulator(object):

    def __init__(
        self,
        no_people=20,
        no_floors=4,
        no_cars=3,
        capacity=[5, 5, 5],
        speed=0.1,
        gui=False,
        id=0,
    ):
        self.no_people = no_people
        self.no_floors = no_floors
        self.no_cars = no_cars
        self.capacity = capacity
        self.speed = speed
        self.gui = gui

        # initialization simpy
        self._env = simpy.RealtimeEnvironment(
            initial_time=0, factor=speed, strict=False
        )

        cars = []
        for idx in range(no_cars):
            cars.append(
                Car(
                    id=idx,
                    env=self._env,
                    no_floors=no_floors,
                    capacity=capacity[idx],
                )
            )
        people = []
        for idx in range(no_people):
            people.append(Person(id=idx, env=self._env, no_floors=no_floors))

        self._state = State(
            cars=cars,
            people=people,
            no_floors=no_floors,
            no_people=no_people,
            no_cars=no_cars,
            id=id,
        )
        self._agent = None

        # initialization pygame
        if self.gui:
            self._screen = Screen(self._state)

        self._waiting_time = 10  # waiting steps after finish simulation

    def register_agent(self, agent: Agent):
        # transfer the state to the agent
        agent.state = self._state
        self._agent = agent

    def run(self):
        """
        Run the simulator!
        :return:
        """
        logging.info(f"INITIAL STATE: {self._state}")

        # Initialization updating of screen
        if self.gui:
            self._env.process(self.screen_update())

        # Initialization updating of directions of the cars
        self._env.process(self.run_update_directions())

        # Init people arriving process and check if all of them arrived
        self._env.process(self.run_arriving_people())

        # Initialization people getting in process
        self._env.process(self.run_getting_in_people())

        # Initialization movement of the cars
        self._env.process(self.run_movement_cars())

        logging.info("SIMULATION START")
        self._env.run()

        logging.info(f"FINAL STATE: {self._state}")

    def run_getting_in_people(self):
        while not self._state.all_people_arrive:
            if self._env.now > 0:
                for person in self._state.people:
                    person.getting_in(self._state.cars)
                    if self._state.no_people == person.id + 1:
                        yield self._env.timeout(self._state.no_cars + 2)
                    else:
                        yield self._env.timeout(1)
            else:
                yield self._env.timeout(1)

    def run_arriving_people(self):
        while not self._state.all_people_arrive:
            if self._env.now > 0:
                no_arrives = 0
                for person in self._state.people:
                    person.arriving(self._state.cars)
                    if person.arrived:
                        no_arrives += 1
                    if no_arrives == self._state.no_people:
                        self._state.all_people_arrive = True
                    if self._state.no_people == person.id + 1:
                        yield self._env.timeout(self._state.no_cars + 2)
                    else:
                        yield self._env.timeout(1)
            else:
                yield self._env.timeout(1)

    def screen_update(self):
        while not (self._state.all_people_arrive and self._waiting_time == 0):
            self._screen.update()
            if self._state.all_people_arrive:
                self._waiting_time -= 1
            yield self._env.timeout(1)

    ########################################################################## TO DO: change for an execute  actions (implement door open and close)
    def run_update_directions(self):
        while not self._state.all_people_arrive:
            # get actions from agent
            actions = self._agent.next_actions()

            # check if the all cars have actions from the controller
            if len(actions) != self._state._no_cars:
                logging.error(
                    f"Number of action {len(actions)} is not equal to number of cars{len(self._state.cars)} at simulation step {self._env.now}"
                )

            # update directions of the cars using actions from agent
            for id_car in range(self._state.no_cars):
                car = self._state.cars[id_car]
                car.direction = actions[id_car]
                logging.info(
                    f"Car {car.id} direction {car.direction} at simulation step {self._env.now}"
                )
            yield self._env.timeout(self._state.no_people + self._state.no_cars + 1)

    def run_movement_cars(self):
        while not self._state.all_people_arrive:
            if self._env.now > self._state.no_people:
                # momevent of the cars according to the directions
                for car in self._state.cars:
                    car.movement()
                    # updating position of people who are in the cars
                    self.update_people_in_cars()
                    if self._state.no_cars == car.id + 1:
                        yield self._env.timeout(self._state.no_people + 2)
                    else:
                        yield self._env.timeout(1)
            else:
                yield self._env.timeout(1)

    def update_people_in_cars(self):
        for person in self._state.people:
            if person.in_car:
                person.current_floor = self._state.cars[person.id_car].current_floor
                logging.info(
                    f"Person {person.id} moves to {person.current_floor} in car {person.id_car} at simulation step {self._env.now}"
                )
