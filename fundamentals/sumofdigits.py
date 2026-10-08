# Ask the user for a number
num = int(input("Enter a number:"))

# Initialize the sum to zero
sum = 0

# Keep dividing the number until it becomes zero
while num > 0:
    # Get the last digit
    lastdigit = num % 10

    # Add the last digit to the running total
    sum = sum + lastdigit

    # Remove the last digit from the number
    num = num // 10

# Print the final sum of digits
print("Sum of digits is:", sum)

        