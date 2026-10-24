# Read the number of rows for the diamond pattern
n = int(input("Enter the number of rows for the top half: "))

# Top half of the diamond: rows decrease from n to 1
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# Bottom half of the diamond: rows increase from 2 to n
for i in range(2, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))