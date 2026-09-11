# Initialize a list of programming languages
languages = ["Python", "Java", "C++"]

# 1. Add elements
languages.append("JavaScript")  # Adds to the end
languages.insert(1, "Ruby")      # Inserts at index 1
print("After additions:", languages)

# 2. Remove elements
languages.remove("Java")         # Removes the first occurrence of "Java"
popped_item = languages.pop()    # Removes and returns the last element
print(f"Popped item: {popped_item}")
print("After removals:", languages)

# 3. Sort the list
languages.sort()
print("Sorted list:", languages)
