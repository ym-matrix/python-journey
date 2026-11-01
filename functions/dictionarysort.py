# Dictionary containing countries and their medal counts
medals = {'Japan': 41, 'Russia': 56, 'South Korea': 21, 'United States': 121, 'Germany': 42, 'China': 70}

# Sort country names by their medal counts in descending order
# The lambda retrieves each country's value from the medals dictionary
top_three = sorted(medals.keys(), key=lambda medal: medals[medal], reverse=True)

# Print all countries ordered from most to least medals
print(top_three)