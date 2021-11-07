import time
from tkinter import Tk, Canvas
from model.person import Person
from model.car import Car


class Display(object):
    def __init__(self, state, animation_speed, name_agent):
        self._state = state
        self._name_agent=name_agent

        self._floor_height = round(600 / self._state.num_floors)  # To animate people. Total size is 600px
        self._arrivals_population = [0] * (self._state.num_floors)
        print(self._state.cars)
        self._elevator_animation = [0] * self._state.cars[0].capacity  # For people inside the elevator

        tk = Tk()
        tk.attributes("-fullscreen", True)
        canvas = Canvas(tk, width=2000, height=1000)
        tk.title('Elevator - {} algorithm'.format(self._name_agent))
        canvas.pack()

        # This is the legend in the animation for how many people are where
        canvas.create_oval(85, 70, 95, 80, fill='black')
        canvas.create_oval(85, 90, 95, 100, fill='white')
        canvas.create_oval(85, 110, 95, 120, fill='green')
        self._waiting_label = canvas.create_text(100, 75, text='Waiting', anchor='w')
        self._inside_label = canvas.create_text(100, 95, text='Inside elevator', anchor='w')
        self._delivered_label = canvas.create_text(100, 115, text='Arrived', anchor='w')
        # This next part sets up the drawing of the floors and labeling them
        for k in range(self._state.num_floors):
            canvas.create_line(50, 200 + (self._state.num_floors - k) * self._floor_height, 600,
                               200 + (self._state.num_floors - k) * self._floor_height)
            canvas.create_text(5, 200 + (self._state.num_floors - k) * self._floor_height,
                               text='Floor ' + str(k), anchor='w')
        canvas.create_rectangle(200, 200, 400, 200 + self._floor_height * self._state.num_floors)  # shaft
        self._elevator = canvas.create_rectangle(203, 200 + self._floor_height * (self._state.num_floors - 1),
                                           397, 200 + self._floor_height * self._state.num_floors,
                                           fill='black')
        tk.update()

        for person in self._state.status['people']:
            offset = self._state.floor_population[person.current_floor] * 13
            person.animation = canvas.create_oval(
                185 - offset,
                # x start
                190 + (self._state.num_floors - person.current_floor) * self._floor_height,
                # y
                195 - offset,  # x finish
                200 + (self._state.num_floors - person.current_floor) * self._floor_height,
                # y
                fill='black')
            tk.update()
            self._state.floor_population[person.current_floor] += 1

        self._animation_speed = animation_speed
        self._canvas = canvas
        self._tk = tk

    def move_slowly(self, animation, x, y):
        """This function animates people entering and exiting the elevator"""
        for j in range(0, 50):
            self._canvas.move(animation, x / 50, y / 50)
            self._tk.update()
            time.sleep(self._animation_speed / 500)

    def arriving_person(self, person, car):
        self._elevator_animation[person.elevator_spot] = False
        self._canvas.itemconfig(person.animation, fill='green')
        self._arrivals_population[car.current_floor] += 1
        self.move_slowly(person.animation, 390 + self._arrivals_population[car.current_floor] * 12 -
                         self._canvas.coords(person.animation)[0], 15 * (person.elevator_spot % 2))
        self._canvas.itemconfig(self._delivered_label, text=f'Arrived - {self._state.num_arrived}')
        self._canvas.itemconfig(self._inside_label, text=f'Inside elevator - {car.in_people}')
        self._canvas.itemconfig(self._waiting_label, text=f'Waiting - {self._state.num_people - self._state.num_arrived}')

    def in_car(self, person, car):
        for spot in range(len(self._elevator_animation)):
            if not self._elevator_animation[spot]:
                self._elevator_animation[spot] = True
                person.elevator_spot = spot
                self.move_slowly(person.animation, (275 + (spot % 3) * 15) -
                            self._canvas.coords(person.animation)[0], -15 * (spot % 2))
                break
        self._canvas.itemconfig(person.animation, fill='white')
        self._canvas.itemconfig(self._inside_label,
                          text='Inside elevator - ' + str(car.in_people))
        self._canvas.itemconfig(self._waiting_label,
                          text=f'Waiting - {self._state.num_people - self._state.num_arrived}')

    def iteraction(self):
        for i in range(self._floor_height):
            self._tk.update()
            time.sleep(self._animation_speed / self._floor_height)
            self._canvas.move(self._elevator, 0, -self._state.status['cars'][0].direction)  # animate the lift moving
            for person in self._state.status['people']:
                if person.in_car:
                    self._canvas.move(person.animation, 0,
                                -self._state.status['cars'][0].direction)  # animate the people moving
        time.sleep(self._animation_speed)

    def finish(self):
        longest_wait_time = max(self._state.wait_times)
        average_wait_time = sum(self._state.wait_times) / self._state.people_number
        self._canvas.create_text(200, 900, text="Average wait time: " + str(round(average_wait_time, 1)),
                           font=("Cambria", 20))
        print('\n\nLongest wait', longest_wait_time)
        print('Shortest wait', min(self._state.wait_times))
        print('Sum of all wait times', sum(self._state.wait_times))
        print(self._state.num_floors, 'floor building with', self._state.people_number, 'people')
        print('Average wait time of', average_wait_time, 'when using', self._name_agent, '\n\n')
        self._tk.mainloop()
