# Ask the user for the number of rows
rows = int(input("Enter number of rows: "))

# Loop through each row from 1 to rows
for i in range(1, rows + 1):
    # Create spaces before the stars to center the pattern
    spaces = " " * (rows - i)
    # Create a row with an odd number of stars
    stars = "*" * (2 * i - 1)

    # Print the spaces and stars for the current row
    print(spaces + stars)