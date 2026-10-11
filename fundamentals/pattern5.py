# Read the size of the pattern
n = int(input("Enter number of rows and columns:"))

# Print rows in descending order, creating a hollow-like pyramid pattern
for i in range(n, 0, -1):
    # Add leading spaces to center the pattern
    space = " " * (n - i)
    # Create the current row with an odd number of stars
    stars = "*" * (2 * i - 1)
    # Print the formatted row
    print(space + stars)