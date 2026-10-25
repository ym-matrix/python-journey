list1 = [8, 3, 4, 5, 6, 7, 9]

tot = 0
for elem in list1:
    tot = tot + elem
accum = 0
index = 0

while index < len(list1):
    accum += list1[index]
    index += 1
print("The total sum of the list is:", accum)