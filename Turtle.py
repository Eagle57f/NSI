from turtle import *

speed(10)


def square(*, pos:tuple, lenght:int):
    up()
    goto(pos)
    down()
    for i in range(4):
        fd(lenght)
        lt(90)

square(pos=(0, 0), lenght=50)
square(pos=(-200, 200), lenght=50)
square(pos=(-200, -200), lenght=50)
square(pos=(200, -200), lenght=50)
square(pos=(200, 200), lenght=50)
