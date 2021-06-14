from turtle import *
import time
velocidad = int(input('Velocidad: '))
setup(1080, 1080, 0, 0)
screensize(2040, 2040)
speed(velocidad)
title("Un vistazo a la mente humana")

for a in range(50):
    forward(100)
    right(90)

    for b in range(1):
        forward(100)
        right(80)

        for c in range(3,11):

            for d in range(c):
                forward(100)
                right(360/c)
hideturtle()

time.sleep(60*5)
