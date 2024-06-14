import pygame
import sys
import logging


class Screen(object):
    def __init__(self, state):
        pygame.init()
        self._colors = {
            "white": (255, 255, 255),
            "black": (0, 0, 0),
            "red": (255, 0, 0),
            "green": (0, 255, 0),
            "blue": (0, 0, 255),
        }

        # define sizes of each element in the screen (in pixels)

        self._space_among_cars = 20
        self._space_among_people = 15
        self._space_between_car_floor = 10

        self._height_car = 120
        self._num_people_in_car = 4
        self._width_car = (self._num_people_in_car + 1) * self._space_among_people

        self._height_floor = self._height_car + self._space_between_car_floor * 2
        self._width_floor = (
            state.no_cars * self._width_car
            + (state.no_cars + 1) * self._space_among_cars
        )

        self._space_building_screen = 10

        self._space_people_width = 500

        self._width_screen = (
            self._width_floor
            + self._space_building_screen * 2
            + self._space_people_width
        )
        self._height_screen = (
            state.no_floors * self._height_floor + self._space_building_screen * 2
        )

        self._surface = pygame.display.set_mode(
            (self._width_screen, self._height_screen)
        )

        self._state = state
        self.update()
        state.people

    def update(self):
        self._surface.fill(self._colors["white"])

        # draw building
        self.draw_building()

        # draw cars
        self.draw_cars()

        # draw people
        self.draw_people()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                logging.info(f"FINAL STATE:" + str(self._state))
                sys.exit()

        pygame.display.flip()

    def draw_building(self):
        for y_pos in range(self._state.no_floors + 1):
            pygame.draw.line(
                surface=self._surface,
                color=self._colors["black"],
                start_pos=(
                    self._space_building_screen,
                    self._space_building_screen + y_pos * self._height_floor,
                ),
                end_pos=(
                    self._space_building_screen + self._width_floor,
                    self._space_building_screen + y_pos * self._height_floor,
                ),
                width=2,
            )

        for x_pos in range(2):
            pygame.draw.line(
                surface=self._surface,
                color=self._colors["black"],
                start_pos=(
                    self._space_building_screen + x_pos * self._width_floor,
                    self._space_building_screen,
                ),
                end_pos=(
                    self._space_building_screen + x_pos * self._width_floor,
                    self._space_building_screen
                    + self._height_floor * self._state.no_floors,
                ),
                width=2,
            )

    def draw_cars(self):
        x_pos = self._space_among_cars + self._space_building_screen
        for car in self._state.cars:
            y_pos = (
                self._height_screen
                - self._space_between_car_floor * 2 * (car.current_floor + 1)
                - self._height_car * (car.current_floor + 1)
            )
            pygame.draw.rect(
                surface=self._surface,
                color=self._colors["black"],
                rect=(x_pos, y_pos, self._width_car, self._height_car),
                width=2,
            )
            x_pos += self._width_car + self._space_among_cars

    def draw_people(self):
        people_floors_no_arrived = [0] * self._state.no_floors
        people_floors_arrived = [0] * self._state.no_floors
        for person in self._state.people:
            if person.arrived:
                people_floors_arrived[person.current_floor] += 1
            elif not person.arrived and not person.in_car:
                people_floors_no_arrived[person.current_floor] += 1

        y_pos = self._height_screen - self._space_building_screen * 3
        for floor in range(self._state.no_floors):
            x_pos = self._width_floor + self._space_among_people * 2
            if people_floors_no_arrived[floor] != 0:
                for i in range(people_floors_no_arrived[floor]):
                    pygame.draw.circle(
                        surface=self._surface,
                        color=self._colors["red"],
                        center=(x_pos, y_pos),
                        radius=5,
                        width=0,
                    )
                    x_pos += self._space_among_people

            if people_floors_arrived[floor] != 0:
                for i in range(people_floors_arrived[floor]):
                    pygame.draw.circle(
                        surface=self._surface,
                        color=self._colors["green"],
                        center=(x_pos, y_pos),
                        radius=5,
                        width=0,
                    )
                    x_pos += self._space_among_people
            y_pos -= self._height_floor

        for car in self._state.cars:
            if car.in_people != 0:
                y_pos = (
                    self._height_screen
                    - self._space_building_screen * 3
                    - self._height_floor * car.current_floor
                )
                x_pos = (
                    self._space_building_screen
                    + self._space_among_cars
                    + self._space_among_people
                    + (self._space_among_cars + self._width_car) * car.id
                )
                for i in range(car.in_people):
                    pygame.draw.circle(
                        surface=self._surface,
                        color=self._colors["blue"],
                        center=(x_pos, y_pos),
                        radius=self._space_among_people / 3,
                        width=0,
                    )
                    if (i + 1) % self._num_people_in_car == 0:
                        y_pos -= self._space_among_people
                        x_pos = (
                            self._space_building_screen
                            + self._space_among_cars
                            + self._space_among_people
                            + (self._space_among_cars + self._width_car) * car.id
                        )
                    else:
                        x_pos += self._space_among_people
