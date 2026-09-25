# Import the turtle graphics module
import turtle

# Create the drawing window
screen = turtle.Screen()

# Create a turtle
t = turtle.Turtle()

# Set the turtle's drawing speed
t.speed()

# Draw a spiral flower pattern
for i in range(36):
    # Move the turtle forward
    t.forward(100)

    # Turn the turtle 170 degrees to the right
    t.right(170)

# Keep the window open
screen.mainloop()

