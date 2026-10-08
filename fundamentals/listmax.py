# Create an empty list to store 10 numbers
numbers = []

# Ask the user to enter 10 numbers and add them to the list
for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)

# Assume the first number is the largest
largest = numbers[0]

# Set second largest to negative infinity so it can be updated later
second = float("-inf")

# Check each remaining number to find the largest and second largest
for n in numbers[1:]:
    if n > largest:
        second = largest
        largest = n
    elif n > second and n != largest:
        second = n

# Print the largest number
print("The largest number is:", largest)

# If no second largest exists, print a message
if second == float("-inf"):
    print("There is no second largest (all numbers are the same)")
else:
    print("The second largest number is:", second)