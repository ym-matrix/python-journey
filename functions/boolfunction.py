# Define a function that looks up a number only when the condition is enabled
def test(num, condition=True, dict1={2: 3, 4: 5, 6: 8}):
    if condition:
        # Return the mapped value when num is a key in the dictionary
        if num in dict1:
            return dict1[num]
    else:
        # Return False when condition is disabled
        return False

# Call the function with the key 4 and print the result
print(test(4))