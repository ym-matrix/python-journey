# Add together the numbers in a list and return the total
def accum(lst):
    sum = 0
    # Add each number to the running total
    for num in lst:
        sum = sum + num
    return sum


# Example list to pass to the function
numbers = [1, 4, 2, 6]
# Print the sum of the numbers
print(accum(numbers))