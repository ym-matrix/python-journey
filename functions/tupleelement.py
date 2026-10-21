# Each tuple contains a city, country, year, and optionally a status
tuples_lst = [
    ("Beijing", "China", 2008),
    ("London", "England", 2012),
    ("Rio", "Brazil", 2016, "Current"),
    ("Tokyo", "Japan", 2020, "Future"),
]

# Gather the country (the second element) from each tuple
country = []
for item in tuples_lst:
    country.append(item[1])

# Display the list of countries
print(country)