# Ask the user for the number of rows and columns
row = int(input("Enter number of rows:"))
col = int(input("Enter number of columns:"))

# Loop through each row
for i in range(1, row + 1):
    # Print letters in increasing order for each row
    for j in range(i):
        print(chr(ord("A") + j), end=" ")
    print()