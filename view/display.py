import time
from tkinter import Tk, Canvas
from model.person import Person
from model.car import Car



class Display(object):
    def __init__(self, animation_speed, floors_number, info_cars):
        self._self._floor_height  = round(600 / floors_number)  # This is for animating people. Total size is 600px
        arrivals_population = [0] * (floors_number + 1)  # This is for animating purposes only
        elevator_animation = [0] * max_elevator_capacity  # This is for people inside the elevator
        tk = Tk()
        tk.attributes("-fullscreen", True)
        canvas = Canvas(tk, width=2000, height=1000)
        tk.title('Elevator - {} algorithm'.format(algorithm))
        canvas.pack()

        

        # This is the legend in the animation for how many people are where
        canvas.create_oval(85, 70, 95, 80, fill='black')
        canvas.create_oval(85, 90, 95, 100, fill='white')
        canvas.create_oval(85, 110, 95, 120, fill='green')
        waiting_label = canvas.create_text(100, 75, text='Waiting', anchor='w')
        inside_label = canvas.create_text(100, 95, text='Inside elevator', anchor='w')
        delivered_label = canvas.create_text(100, 115, text='Arrived', anchor='w')
        # This next part sets up the drawing of the floors and labeling them
        for k in range(floors_number):
            canvas.create_line(50, 200 + (floors_number - k) * self._floor_height , 600,
                               200 + (floors_number - k) * self._floor_height )
            canvas.create_text(5, 200 + (floors_number - k) * self._floor_height ,
                               text='Floor ' + str(k), anchor='w')
        canvas.create_rectangle(200, 200, 400, 200 + self._floor_height  * floors_number)  # shaft
        elevator = canvas.create_rectangle(203, 200 + self._floor_height  * (floors_number - 1),
                                           397, 200 + self._floor_height  * floors_number, fill='black')
        tk.update()
        self._animation_speed=animation_speed
        self._canvas=canvas
        self._tk=tk

    def move_slowly(self,animation, x, y):
        """This function animates people entering and exiting the elevator"""
        for j in range(0, 50):
            self._canvas.move(animation, x / 50, y / 50)
            self._tk.update()
            time.sleep(self._animation_speed / 500)








if animate:  # this sets up the canvas with the elevator and floors etc if animate is true
    

if animate:
    offset = floor_population[s_f] * 13
    person.animation = canvas.create_oval(185 - offset,  # x start
                                          190 + (floors_number - s_f) * self._floor_height ,
                                          # y
                                          195 - offset,  # x finish
                                          200 + (floors_number - s_f) * self._floor_height ,
                                          # y
                                          fill='black')
    tk.update()
