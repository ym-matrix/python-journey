# Sample list of numbers to sum.
list1 = [8, 3, 4, 5, 6, 7, 9]

# Total using a for loop.
tot = 0
for elem in list1:
    tot = tot + elem

# Total using a while loop.
accum = 0
index = 0

while index < len(list1):
    accum += list1[index]
    index += 1

# Print the final sum.
print("The total sum of the list is:", accum)