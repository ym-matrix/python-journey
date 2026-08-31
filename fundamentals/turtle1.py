import turtle                  #import the turtle graphics module
wn = turtle.Screen()           #create a graphics window
wn.bgcolor("black")            #set background color to black
alex=turtle.Turtle()           #create a turtle named alex
alex.color("orange")
alex.pensize(5)                #set the pen size to 5

alex.forward(150)              #method to move the turtle forward by 150 units
alex.left(90)                   #method to turn the turtle left by 90 degrees
alex.forward(150)
alex.left(45)
alex.forward(105)
alex.left(90)
alex.forward(105)
alex.left(45)
alex.forward(150)

wn.exitonclick()