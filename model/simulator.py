from model.state import State
from controller.agent import Agent
import copy


class Simulator(object):

    def __init__(self, people_number=2, floors_number=2, info_cars=None):
        if info_cars is None:
            info_cars = {"car_number": 1, "capacity": [1]}
        self._people_number=people_number
        self._floors_number=floors_number
        self._info_cars=info_cars
        self._all_done = False
        self._state = State(self._people_number, self._floors_number, self._info_cars)
        self._agent = None

    def register_agent(self, agent: Agent):
        self._agent = agent

    def _update_state(self, status: dict):
        self._state.status = status

    def run(self):
        """
        Run the simulator!
        :return:
        """
        assert self._agent is not None

        # self._logger.info(f"Simulator is now ready!")

        # Let the agent know that simulator has initialised
        # Ideally, copy should be implemented within the state class to only copy relevant variables.
        # status = copy.deepcopy(self._state.status)

        while self._state.status['arrived_people_number'] < self._people_number:
            for car in self._state.status['cars']:
                for person in self._state.status['people']:
                    # This measures the wait time of each person by one unit everytime the lift moves
                    # It includes time spent in the lift. It only stops counting when they have arrived
                    if not person.arrived:
                        person.wait_time += 1

                        if car.floor == person.current_floor:
                            if person.in_elevator:
                                if car.floor == person.target_floor:
                                    person.in_elevator = False
                                    person.arrived = True
                                    car.in_people -= 1
                                    self._state.status['arrived_people_number']+=1
                                else:
                                    person.current_floor += car.direction
                            else:
                                if not car.full and car.direction == person.direction:
                                    person.in_elevator = True
                                    car.in_people += 1
                car.floor += car.direction


        #             if not car.full and not person.arrived and car.floor==person.current_floor:
        #                 # This is the routine for a person leaving the elevator on their desired floor
        #
        #                 elif person.in_elevator and car.floor != person.target_floor:
        #                     person.current_floor += car.direction
        #                 elif not person.in_elevator and (person.target_floor)
        #
        #
        #         if person.in_elevator and person.arrived(elevator_floor):
        #             person.in_elevator = False
        #             person.finished = True
        #             elevator_population.remove(person)
        #
        #     for person in total_population:  # for people to get into the elevator
        #         if person.waiting() and person.start_floor == elevator_floor and len(
        #                 elevator_population) < max_elevator_capacity and (
        #                 (
        #                         elevator_direction == person.direction or elevator_floor == 0 or elevator_floor == number_of_floors - 1 or elevator_floor == target_floor)):  # person gets in
        #             elevator_population.append(person)
        #             person.in_elevator = True
        #             floor_population[elevator_floor] -= 1
        #
        #     if sum(floor_population) + len(elevator_population) == 0:
        #         break
        #
        #     elevator_floor += elevator_direction  # The lift moves one floor
        # wait_times = []
        # for person in total_population:
        #     if not person.finished:
        #         print('Somethings gone wrong')
        #     wait_times.append(person.wait_time)
        #
        # longest_wait_time = max(wait_times)
        # average_wait_time = sum(wait_times) / number_of_people
