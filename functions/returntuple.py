def information(name, birth_year, fav_color, hometown):
    return (name, birth_year, fav_color, hometown)

name = input("Name: ")
year = int(input("Birth year: "))
color = input("Favorite color: ")
town = input("Hometown: ")

result = information(name, year, color, town)
print(result)