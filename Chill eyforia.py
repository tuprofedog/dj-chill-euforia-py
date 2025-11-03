#Pixel Art - http://www.101computing.net/pixel-art-in-python/
import turtle
from config import *
from time import sleep
from random import randint, choice, random

myPen = turtle.Turtle()

# This function draws a box by drawing each side of the square and using the fill function
def box(intDim):
    myPen.begin_fill()
    # 0 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 90 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 180 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 270 deg.
    myPen.forward(intDim)
    myPen.end_fill()
    myPen.setheading(0)

def drawPixelArt(pixelArt, colors, boxSize):
    # Draw the pixel art
    for i in range (0,len(pixelArt)):
        for j in range (0,len(pixelArt[i])):
            if pixelArt[i][j] != 0:
                myPen.color(colors[pixelArt[i][j]-1])
                box(boxSize)
            myPen.penup()
            myPen.forward(boxSize)
            myPen.pendown()	
        myPen.setheading(270) 
        myPen.penup()
        myPen.forward(boxSize)
        myPen.setheading(180) 
        myPen.forward(boxSize*len(pixelArt[i]))
        myPen.setheading(0)
        myPen.pendown()
    
    myPen.getscreen().update()	
	
# Returns the rotated list
def rightRotate(lists, num):
    output_list = []

    # Will add values from n to the new list
    for item in range(len(lists) - num, len(lists)):
        output_list.append(lists[item])

    # Will add the values before
    # n to the end of new list
    for item in range(0, len(lists) - num):
        output_list.append(lists[item])

    return output_list

def drawBg():
    screen_width = turtle.window_width()
    screen_height = turtle.window_height()

    for x in range(-int(screen_width/2), int(screen_width/2), randint(25,75)):
        for y in range(-int(screen_height/2), int(screen_height/2), randint(25,75)):
            myPen.penup()
            myPen.goto(x, y)
            myPen.pendown()
            myPen.color(choice(COLORS_2), choice(COLORS_2))
            if random() < 0.5:  # 50% chance to fill
                myPen.begin_fill()
            myPen.circle(randint(1,10), steps=randint(3,10))
            if myPen.filling():  # only end if it was filling
                myPen.end_fill()

for i in range(1, len(COLORS_1) + 1):
    for j in range(0, len(COLORS_1)):
        turtle.clearscreen()

        # Initial config
        myPen._tracer(0)
        num = randint(15,25)

        for i in range(5):
            drawBg()

            # Position myPen in top left area of the screen
            myPen.penup()
            myPen.goto(0, 0)
            myPen.forward(-400) # Horizontal position adjusted
            myPen.setheading(90)
            myPen.forward(250) # Vertical position adjusted
            myPen.setheading(0)

            # Draw the pixel art and rotate colors
            drawPixelArt(FACE_1, COLORS_1, num)

        COLORS_1 = rightRotate(COLORS_1, i)