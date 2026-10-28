# Return items from the list up to the first "bye" or a maximum of 10 items
def beginning(str):
    sublist = []
    idx = 0

    # Keep looping while there are fewer than 10 items and "bye" has not been found
    while idx < 10 and str[idx] != 'bye':
        sublist.append(str[idx])
        idx += 1

    return sublist

# Test the function with a sample list
print(beginning(['Hi', 'My', 'Name', 'Is', 'Jack', 'Sparow', 'What', 'Do', 'you', 'want', 'that', 'i', 'have', 'bye']))