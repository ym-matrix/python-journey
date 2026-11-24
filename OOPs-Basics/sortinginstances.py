class Fruit():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __lt__(self, other): 
        return self.name < other.name 
apple = Fruit("Apple", 10)
cherry = Fruit("Cherry", 5)
blueberry = Fruit("Blueberry", 20)
L = [cherry, apple, blueberry]

print("-----sorted using comparison operator (without key)-----")
for f in sorted(L):
    print(f.name)

print(f'apple < cherry: {apple < cherry}')