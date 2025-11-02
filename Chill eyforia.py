#Pixel Art - http://www.101computing.net/pixel-art-in-python/
import turtle
from config import *

myPen = turtle.Turtle()
myPen._tracer(0)
myPen.speed(0)
boxSize = 25

# Position myPen in top left area of the screen
myPen.penup()
myPen.goto(0, 0)
myPen.forward(-400) # Horizontal position adjusted
myPen.setheading(90)
myPen.forward(250) # Vertical position adjusted
myPen.setheading(0)

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

def drawPixelArt(pixelArt, colors):
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
	
drawPixelArt(FACE_1, COLORS_1)

from time import sleep
sleep(5)