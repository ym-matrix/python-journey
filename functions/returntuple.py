# Collect the supplied details into a tuple
def information(name, birth_year, fav_color, hometown):
    return (name, birth_year, fav_color, hometown)

# Ask the user for each piece of information
name = input("Name: ")
year = int(input("Birth year: "))
color = input("Favorite color: ")
town = input("Hometown: ")

# Create and display the tuple of details
result = information(name, year, color, town)
print(result)