# Ask the user to enter a number
num = int(input("Enter a number:"))

# Store the original number for comparison later
temp = num

# If the number is 0, it is not a valid Armstrong number
if num == 0:
    print("Enter valid number")
else:
    # Initialize the sum of digits raised to the power of the number of digits
    sum = 0

    # Calculate the number of digits in the number
    power = len(str(num))

    # Loop through each digit in the number
    for d in str(num):
        # Get the last digit
        lastdigit = num % 10

        # Remove the last digit from the number
        num = num // 10

        # Add the digit raised to the power to the sum
        sum = sum + lastdigit ** power

    # Check if the original number matches the computed Armstrong value
    if temp == sum:
        print(f"{temp} is an armstrong number")
    else:
        print(f"{temp} is not an armstrong number")
       

