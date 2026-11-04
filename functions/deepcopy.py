# Create the original nested list with two inner lists
original = [['dogs', 'puppies'], ['cats', "kittens"]]

# Copy the outer list and every inner list separately
copied_outer_list = []
for inner_list in original:
    copied_inner_list = []
    for item in inner_list:
        copied_inner_list.append(item)
    copied_outer_list.append(copied_inner_list)

# Display the copied nested list
print(copied_outer_list)

# Add a new nested item to the first inner list in the original
original[0].append(["canines"])

# Show that the original changed
print(original)

# The copied list remains unchanged because its inner lists were copied separately
print("-------- Now look at the copied version -----------")
print(copied_outer_list)