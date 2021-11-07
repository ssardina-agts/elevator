from model.state import State
from controller.agent import Agent
from view.display import Display
import copy


class Simulator(object):

    def __init__(self, people_number=2, floors_number=2, cars=[1]):
        self._all_done = False
        self._state = State(people_number, floors_number, cars)

        self._agent = None

    def register_agent(self, agent: Agent):
        self._agent = agent

    def run(self, animation_speed=0.1):
        """
        Run the simulator!
        :return:
        """
        assert self._agent is not None
        self._display = Display(self._state, animation_speed, self._agent.name)

        print('INITIAL STATE:')
        self._state.print()

        while self._state.num_arrived < self._state.num_people:

            # get the actions per car
            actions = self._agent.next_actions(self._state)

            idx_car = 0
            for car in self._state.cars:
                car.direction = actions['directions'][idx_car]
                car.target_floor = actions['targets'][idx_car]

                for person in self._state.people:
                    if person.in_car:
                        if car.current_floor == person.target_floor:
                            person.in_car = False
                            person.arrived = True
                            car.in_people -= 1
                            self._state.floor_population[car.current_floor] -= 1
                            self._state.num_arrived += 1
                            self._display.arriving_person(person, car)

                        else:
                            person.current_floor += car.direction
                            person.wait_time += 1

                for person in self._state.people:
                    # This measures the wait time of each person by one unit everytime the lift moves
                    # It includes time spent in the lift. It only stops counting when they have arrived
                    if not person.arrived and not person.in_car:
                        if car.current_floor == person.current_floor and not car.full and car.direction == person.direction:
                            person.in_car = True
                            person.current_floor += car.direction
                            car.in_people += 1
                            self._display.in_car(person, car)
                        person.wait_time += 1

                car.current_floor += actions['directions'][idx_car]
            self._display.iteraction()
            self._state.print()
        print(self._state.wait_times)

        self._display.finish()
