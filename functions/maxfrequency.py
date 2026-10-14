# String containing the text to analyze
sally = "sally sells sea shells by the sea shore"

# Dictionary to store the frequency of each character
characters = {}
best_char = ''

# Count each character in the string
for achar in sally:
    if achar in characters:
        characters[achar] += 1
    else:
        characters[achar] = 1

# Show the frequency dictionary for reference
print(characters)

# Find the most frequent character excluding the space
best_count = 0
for char in characters:
    if char != " " and characters[char] > best_count:
        best_count = characters[char]
        best_char = char

# Print the character with the maximum frequency
print(best_char)