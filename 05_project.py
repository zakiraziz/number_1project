from turtle import *
import colorsys as cs

speed(0)
bgcolor("black")
h = 0.1
pensize(3)

for i in range(80):
    c = cs.hsv_to_rgb(h,1,1)
    color(c)
    h +=0.1
    for j in range(17):
        fd(0.2*i*j)
        lt(33/0.001)

done()