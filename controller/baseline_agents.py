import asyncio
import time
import numpy as np
from controller.agent import Agent
import coloredlogs
import logging
from model.state import State


class Baseline(Agent):
    def __init__(self):
        super().__init__("Baseline Agent")

    def next_actions(self, state: State) -> dict:
        actions = {}
        if car.current_floor != 0 and car.current_floor != state.num_floors - 1:
            actions[car.id] = (car.direction, car.target_floor)
        elif car.current_floor == 0:
            actions[car.id] = (1, state.num_floors- 1)
        else:
            actions[car.id] = (-1, 0)
        return actions


class Efficient(Agent):
    def __init__(self):
        super().__init__("Efficient Agent")

    def next_actions(self, state: State) -> dict:
        directions = []
        targets = []

        elevator_buttons = [False] * state.num_floors  # reset elevator buttons

        for person in state.status['people']:
            if person.in_car:
                elevator_buttons[person.target_floor] = True
        floors_people_want_to_go_to = [i for i in range(len(elevator_buttons)) if
                                       elevator_buttons[i]]  # in elevator
        for car in state.cars:
            if not car.full:
                floors_people_want_to_go_to.extend([floor for floor in range(state.num_floors) if
                                                    bool(state.floor_population[floor])])  # on floors
            highest_floor = max(floors_people_want_to_go_to)
            lowest_floor = min(floors_people_want_to_go_to)
            if car.direction == -1:
                target_floor = lowest_floor
            else:
                target_floor = highest_floor
            elevator_direction = -1 if target_floor < car.current_floor else 1
            if car.current_floor == target_floor:
                elevator_direction *= -1

            directions.append(elevator_direction)
            targets.append(target_floor)

        return {"directions": directions, "targets": targets}

        # elevator_buttons = [False] * number_of_floors  # reset elevator buttons
        # for person in elevator_population:
        #     elevator_buttons[person.target_floor] = True
        # floors_people_want_to_go_to = [i for i in range(len(elevator_buttons)) if
        #                                elevator_buttons[i]]  # in elevator
        # if len(elevator_population) < max_elevator_capacity:
        #     floors_people_want_to_go_to.extend([floor for floor in range(number_of_floors) if
        #                                         bool(floor_population[floor])])  # on floors
        # highest_floor = max(floors_people_want_to_go_to)
        # lowest_floor = min(floors_people_want_to_go_to)
        # if elevator_direction == -1:
        #     target_floor = lowest_floor
        # elif elevator_direction == 1:
        #     target_floor = highest_floor
        # elevator_direction = -1 if target_floor < elevator_floor else 1
        # if elevator_floor == target_floor:
        #     elevator_direction *= -1

# if algorithm == "baseline":
#     if elevator_floor == 0:
#         elevator_direction = 1
#         target_floor = number_of_floors - 1
#     elif elevator_floor == number_of_floors - 1:
#         elevator_direction = -1
#         target_floor = 0
# elif algorithm == "inefficient":
#     if len(elevator_population) == max_elevator_capacity and target_floor == elevator_floor:
#         # if the elevator is full, then conduct a vote of the people inside.
#         elevator_buttons = [False] * number_of_floors  # reset elevator buttons
#         for person in elevator_population:
#             elevator_buttons[person.target_floor] = True
#         directional_vote = sum(
#             [1 if floor > elevator_floor else -1 for floor in elevator_buttons if floor])
#         highest_floor = max([i for i in range(number_of_floors) if elevator_buttons[i]])
#         lowest_floor = min([i for i in range(number_of_floors) if elevator_buttons[i]])
#         if animate:
#             print(
#                 "\ndirectional vote is {} with the lowest being {} and the highest {}".format(
#                     directional_vote, lowest_floor, highest_floor))
#         if directional_vote == 0:
#             assert lowest_floor < elevator_floor, 'lowest_floor={}, elevator_floor={}'.format(
#                 lowest_floor, elevator_floor)
#             assert highest_floor > elevator_floor, 'highest_floor={}, elevator_floor={}'.format(
#                 highest_floor, elevator_floor)
#             # it goes the shortest distance to get half the people
#             if elevator_floor - lowest_floor < highest_floor - elevator_floor:
#                 target_floor = lowest_floor
#             elif elevator_floor - lowest_floor > highest_floor - elevator_floor:
#                 target_floor = highest_floor
#             else:  # if they are equal it will go down
#                 target_floor = highest_floor
#                 print('Biased towards down when people waiting')
#         elif directional_vote > 0:
#             target_floor = highest_floor
#         elif directional_vote < 0:
#             target_floor = lowest_floor
#
#     elif target_floor == elevator_floor and sum(floor_population) + len(
#             elevator_population) > 0:
#         # otherwise, combine a vote of everyone who has not arrived
#         elevator_buttons = [False] * number_of_floors  # reset elevator buttons
#         for person in elevator_population:
#             elevator_buttons[person.target_floor] = True
#         elevator_directional_vote = sum(
#             [1 if floor > elevator_floor else -1 for floor in range(len(elevator_buttons))
#              if
#              elevator_buttons[floor]])
#         floor_directional_vote = 0
#         for i in range(number_of_floors):
#             if bool(floor_population[i]):  # If the button has been pressed on each floor
#                 if i > elevator_floor:
#                     floor_directional_vote += 1
#                 elif i < elevator_floor:
#                     floor_directional_vote -= 1
#         directional_vote = elevator_directional_vote + floor_directional_vote
#         if animate:
#             print("combined directional vote of", directional_vote, "made up of",
#                   elevator_directional_vote, "from people inside the elevator and",
#                   floor_directional_vote, "from people waiting on floors")
#         floors_people_want_to_go_to = [i for i in range(len(elevator_buttons)) if
#                                        elevator_buttons[i]]  # in elevator
#         floors_people_want_to_go_to.extend([floor for floor in range(number_of_floors) if
#                                             bool(floor_population[floor])])  # on floors
#         highest_floor = max(floors_people_want_to_go_to)
#         lowest_floor = min(floors_people_want_to_go_to)
#         if directional_vote == 0:
#             assert sum(floor_population) + len(elevator_population) > 0
#             assert lowest_floor < elevator_floor, 'lowest_floor={}, elevator_floor={}. {}(floors={}, people={}) people waiting(onfloors={}, inelevator={})'.format(
#                 lowest_floor, elevator_floor, algorithm, number_of_floors, number_of_people,
#                 sum(floor_population), len(elevator_population))
#             assert highest_floor > elevator_floor, 'highest_floor={}, elevator_floor={}'.format(
#                 highest_floor, elevator_floor)
#             # it goes the shortest distance to get half the people
#             if elevator_floor - lowest_floor < highest_floor - elevator_floor:
#                 target_floor = lowest_floor
#             elif elevator_floor - lowest_floor > highest_floor - elevator_floor:
#                 target_floor = highest_floor
#             else:  # if they are equal it will go down
#                 target_floor = highest_floor
#                 # print('Biased towards down when people waiting')
#         elif directional_vote > 0:
#             target_floor = highest_floor
#         elif directional_vote < 0:
#             target_floor = lowest_floor
#     if target_floor <= -1 or target_floor >= number_of_floors:
#         print('ERROR: target floor:', target_floor, ', elevator floor:', elevator_floor)
#     if (elevator_floor >= number_of_floors or elevator_floor < 0) and animate:
#         print('Massive error has occured. Train off rails. Elevator is on floor',
#               elevator_floor)
#     if elevator_floor == -2 or elevator_floor == number_of_floors + 2:
#         print("elevator is on floor", elevator_floor)
#         exit()
#     elevator_direction = 1 if target_floor > elevator_floor else -1
# elif algorithm == "efficient":  # This is the more efficient solution than the baseline
#     elevator_buttons = [False] * number_of_floors  # reset elevator buttons
#     for person in elevator_population:
#         elevator_buttons[person.target_floor] = True
#     floors_people_want_to_go_to = [i for i in range(len(elevator_buttons)) if
#                                    elevator_buttons[i]]  # in elevator
#     if len(elevator_population) < max_elevator_capacity:
#         floors_people_want_to_go_to.extend([floor for floor in range(number_of_floors) if
#                                             bool(floor_population[floor])])  # on floors
#     highest_floor = max(floors_people_want_to_go_to)
#     lowest_floor = min(floors_people_want_to_go_to)
#     if elevator_direction == -1:
#         target_floor = lowest_floor
#     elif elevator_direction == 1:
#         target_floor = highest_floor
#     elevator_direction = -1 if target_floor < elevator_floor else 1
#     if elevator_floor == target_floor:
#         elevator_direction *= -1
#
