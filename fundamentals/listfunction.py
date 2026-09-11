
languages = ["Python", "Java", "C++"]

# 1. Add elements
languages.append("JavaScript")  
languages.insert(1, "Ruby")      
print("After additions:", languages)


languages.remove("Java")         
popped_item = languages.pop()    
print(f"Popped item: {popped_item}")
print("After removals:", languages)


languages.sort()
print("Sorted list:", languages)

