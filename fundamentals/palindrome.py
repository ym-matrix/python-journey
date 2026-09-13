user_word = input("Enter a word:")

# 1. Clean the word so capitalization doesn't break the check
clean_word = user_word.lower()

# Use string slicing with a step of -1 to reverse it
reversed_word = clean_word[::-1]

print(f"Original: {clean_word}")
print(f"Reversed: {reversed_word}")

if clean_word == reversed_word:
    print(f"Yes, '{user_word}' is a palindrome!")
else:
    print("No, it is not a palindrome.")
