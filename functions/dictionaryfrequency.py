# Input string whose character frequencies will be counted
str1 = "peter piper picked a peck of pickled peppers"

# Dictionary to hold each character and its count
freq = {}

# Loop through each character and update its count
for achar in str1:
    if achar not in freq:
        freq[achar] = 0
    freq[achar] += 1

# Print the character frequency dictionary
print(freq)