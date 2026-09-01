import turtle
wn=turtle.Screen()
wn.bgcolor("black")       #Two spirals are drawn on the screen,using two turtles.                         
max.shape("turtle")       
max.color("white")
dist=1

for i in range(120):
    max.forward(dist)
    max.left(45)
    dist+=1

alex=turtle.Turtle()
alex.speed(10)
alex.shape("arrow")
alex.color("blue")
dist=10

for i in range(150):
    alex.forward(dist)
    alex.right(89)
    dist+=2

wn.mainloop()