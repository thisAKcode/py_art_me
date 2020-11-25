from turtle import *
import random
COLORS = ['blue', 'purple', 'cyan', 'white', 'yellow', 'green', 'orange', 
          'aquamarine', 'plum', 'dark orchid', 'LimeGreen', 'goldenrod', 'lemon chiffon'] 

Screen().bgcolor('turquoise')
# ==============================
# draw snowflakes
from turtle import forward as fd
from turtle import backward as bd
from turtle import left as l
from turtle import right as r

reset()

color('dark orchid')
pensize(4)

# define function vform that is used to draw the first part

def vform2(stor):
    speed(10000)
    r(25)
    fd(stor)
    bd(stor)
    l(50)
    fd(stor)
    bd(stor)
    r(25)

def flakearm(stor):
    for x in range(0,4):
        forward(stor)
        vform2(stor)
    backward(stor*4) # multoply it by 4 so that turtle can beguin again

def flake_making(stor):
    #color(random.choice(COLORS)) # when need one colored flake, placed over for loop
    for x in range(0,6):
        color(random.choice(COLORS)) # when need multicolored flake, place it over for loop
        flakearm(stor)
        right(60)
for i in range(0,10):
    stor = random.randint(5,30)
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    penup()
    goto(x,y)
    pendown()
    flake_making(stor)
#flake_making()
'''reset()
color('white')
pensize(4)

def flake_making_18arm():
    for x in range(0,18):
        color(random.choice(COLORS))
        flakearm()
        right(20) # 18 arm with 20 degrees between each = 360
flake_making_18arm()     
reset()
color('white')
pensize(4)

def flake_making_10arm():
    for x in range(0,10):
        color(random.choice(COLORS))
        flakearm()
        right(36) # 10 arm with 36 degrees between each= 360   
flake_making_10arm()

'''