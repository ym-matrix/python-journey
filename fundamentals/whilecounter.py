# Create an empty list to store even numbers.
# Start counting from zero.
eve_nums = []
counter = 0

# Continue looping while the counter is 15 or less.
while counter <= 15:
    # Add the current number only if it is even.
    if counter % 2 == 0:
        eve_nums.append(counter)
    # Move to the next number.
    counter += 1

# Display the list of even numbers.
print(eve_nums)