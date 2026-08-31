import turtle
screen=turtle.Screen()
screen.bgcolor("Red")
ted=turtle.Turtle()
ted.shape("circle")            #Assigning the shape of turtle to circle
ted.color("Blue")              #changing the turtle color to blue
ted.pencolor("white")
ted.pensize(4)
ted.speed(20)

for i in range(45):            #Loop iterates 45 times 
    ted.circle(40)             #draws shaped circle with radius 40
    ted.forward(30) 
    ted.left(10)

screen.mainloop()             
    
