class Fruit():
    # Store the fruit name and price
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # Allow Fruit instances to be compared by name
    def __lt__(self, other): 
        return self.name < other.name 

# Create Fruit objects
apple = Fruit("Apple", 10)
cherry = Fruit("Cherry", 5)
blueberry = Fruit("Blueberry", 20)

# Add the objects to a list in unsorted order
L = [cherry, apple, blueberry]

# Sort using the Fruit.__lt__ method, without a key function
print("-----sorted using comparison operator (without key)-----")
for f in sorted(L):
    print(f.name)

# Check whether Apple comes before Cherry alphabetically
print(f'apple < cherry: {apple < cherry}')