# Ask the user to enter two words
word1 = input("Enter a word:")
word2 = input("Enter another word:")

# Convert both words to lowercase and sort their letters
cleaned_word1 = sorted(word1.lower())
cleaned_word2 = sorted(word2.lower())

# Compare the sorted letters to check if they are anagrams
if cleaned_word1 == cleaned_word2:
    print(f"'{word1}' and '{word2}' are anagrams!")
else:
    print("Not anagrams.")