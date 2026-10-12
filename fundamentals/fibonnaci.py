# Read how many Fibonacci numbers the user wants to display
n = int(input("Enter number of terms: "))

# Print a header for the series
print("Fibonacci series:\n")

# Initialize the first two numbers of the sequence
a, b = 0, 1

# Generate and print the next n Fibonacci numbers
for i in range(n):
    print(a)
    a, b = b, a + b
