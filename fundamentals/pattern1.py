# Ask the user for the number of rows and columns
n = int(input("Enter number of rows and columns:"))

# Loop through each row from 1 to n
for i in range(1, n + 1):
    # Print '*' i times in this row
    for j in range(i):
        print("*", end=" ")
    print()