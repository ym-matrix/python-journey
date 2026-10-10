# Ask the user for the number of rows and columns
n = int(input("Enter number of rows and columns: "))

# Loop from the entered number down to 1
for i in range(n, 0, -1):
    # Print '*' i times in each row
    for j in range(i):
        print("*", end=" ")
    print()