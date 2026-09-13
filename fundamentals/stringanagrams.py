word1 = input("Enter a word:")
word2 = input("Enter another word:")

cleaned_word1 = sorted(word1.lower())
cleaned_word2 = sorted(word2.lower())

if cleaned_word1 == cleaned_word2:
    print(f"'{word1}' and '{word2}' are anagrams!")
else:
    print("Not anagrams.")
