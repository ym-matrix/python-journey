# Read the number of rows and columns for the pattern
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Print the border rows as full hashes and the middle rows with spaces inside
for i in range(rows):
    if i == 0 or i == rows - 1:
        # Top and bottom rows: full line of hashes
        print("#" * cols)
    else:
        # Middle rows: hash, spaces, and hash
        print("#" + " " * (cols - 2) + "#")