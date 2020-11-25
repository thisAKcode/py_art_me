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

def vform2():
    speed(200)
    r(25)
    fd(50)
    bd(50)
    l(50)
    fd(50)
    bd(50)
    r(25)

def flakearm():
    for x in range(0,4):
        forward(30)
        vform2()
    backward(120)

def flake_making():
    for x in range(0,6):
        color(random.choice(COLORS))
        flakearm()
        right(60)
        
flake_making()
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