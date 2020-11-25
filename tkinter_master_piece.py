import tkinter
print('you draw holding in left mouse button, and pulling cursor')
print('click on color when needed change the color')

'''
figures in tkinter
create_line()
create_rectrangle()
create_oval()
'''

window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=750, height=500, bg='white') # zero is top left
# .Canvas() create an empty drawing surface
#arg 2,3,4 for size , color of canvas
canvas.pack() # place canvas in tkinter window
musX, musY = 0,0 
color = 'black'

# function that store mouse position
def lagra_position(event):
    global musX, musY # makes that function come to var from line 10: musX, musY
    musX = event.x
    musY = event.y # keep an eye on mouse position
    
# create a func that tells what is going to happen when user clicks on canvas 
# store clickposition by calling lagra_position
def vid_click(event): # event is mouse click
    lagra_position(event) 

# add one more function adding line when cursor moved
def vid_drag(event):
    canvas.create_line(musX, musY, event.x, event.y, fill = color,  width = 3) # create line is built in
    '''musX, musY contains cursor coordinates latest clicked or pulled(start position)
event.x event.y contains current x y of place cursor was moved to'''
    lagra_position(event) # store cursor position when you stop to pull mouse

# bind connect code to canvas
canvas.bind('<Button-1>', vid_click) # binds clicks to func vid_klick()
canvas.bind('<B1-Motion>', vid_drag) # mouse moving while left button pressed 



# add a palette with clickable squares with colors
red_id = canvas.create_rectangle(10, 10, 30, 30, fill = 'red') # when create object(here square), it must have an id
blue_id = canvas.create_rectangle(10, 35, 30, 55, fill = 'blue')
black_id = canvas.create_rectangle(10, 60, 30, 80, fill = 'black')
white_id = canvas.create_rectangle(10, 85, 30, 105, fill = 'white')


# function for each color in palett
def choose_color_red(event): # here paremeter event is click on red square
    global color # global that you can change the global var 'color'
    color = 'red'
    
def choose_color_blue(event):
    global color
    color = 'blue'

def choose_color_black(event):
    global color
    color = 'black'

def choose_color_white(event): # good to have to erase stuff
    global color
    color = 'white'

# use tag_bind() to bind event (click on square) to object (color function in previuos step)
canvas.tag_bind(red_id, '<Button-1>', choose_color_red)
canvas.tag_bind(blue_id, '<Button-1>', choose_color_blue)
canvas.tag_bind(black_id, '<Button-1>', choose_color_black)
canvas.tag_bind(white_id, '<Button-1>', choose_color_white)

window.mainloop() # run program
