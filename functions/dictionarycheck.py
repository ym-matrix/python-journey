# Check whether a key exists in a dictionary in one of two directions
def checkingIfIn_2(a, direction=True, d={'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    # When direction is True, return the key's value if it exists
    if direction == True:
        if a in d:
            return d[a]
        else:
            return False
    else:
        # When direction is False, return True if the key is not in the dictionary
        if a not in d:
            return True
        else:
            return d[a]

# Test the function with the key "Apple"
print(checkingIfIn_2("Apple"))