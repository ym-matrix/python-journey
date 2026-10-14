sally = "sally sells sea shells by the sea shore"
characters = {}
best_char = ''
for achar in sally:
    if achar in characters:
        characters[achar] += 1
    else:
        characters[achar] = 1
print(characters)
best_count = 0                        
for char in characters:
    if char != " " and characters[char] > best_count:
        best_count = characters[char] 
        best_char = char              

print(best_char)