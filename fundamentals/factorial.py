# Read the number from user input
n = int(input("Enter a number: "))

# Start with 1 because multiplying by 1 keeps the value unchanged
fact = 1

# Multiply from 1 up to n to compute the factorial
for i in range(1, n + 1):
    fact = fact * i

# Display the computed factorial
print("Factorial = {}".format(fact))