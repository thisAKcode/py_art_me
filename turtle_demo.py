from turtle import *
from time import sleep

# create coloured background
Screen().bgcolor('turquoise')
hideturtle()
color('goldenrod') # blue,aquamarine, cyan, plum, dark orchid, LimeGreen, goldenrod, lemon chiffon, 
# HotPink, DarkKhaki, DarkOrange
shape('turtle') # arrow, circle, square, triangle, classic
speed(5)
pensize(4)

# how turtle is moving

'''
       360/0
    270__!___90
         !
        180
'''
# square
forward(50)
right(90) # right() respectively left() are functions to rotate turtle 
forward(50)
right(90)
forward(50)
right(90)
forward(50)

# Triangle
forward(50)
left(120)
forward(50)
left(120)
forward(50)

# Oktagon
for x in range(8):
    forward(50)
    right(45)
    
sleep(1)


