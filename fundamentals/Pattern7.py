n = int(input("Enter the number of rows for the top half: "))

# top half (pyramid going up)
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# bottom half (pyramid going down)
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))