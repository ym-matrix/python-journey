# Import the math module to use pi
import math

# Ask the user for the radius of the circle and convert it to an integer
r = int(input("Please enter the radius of the circle: "))

# Calculate the area of the circle using the formula A = πr²
area = math.pi * (r ** 2)

# Display the calculated area
print("area of the circle is:", area)
