# Define a base class that provides swimming behavior
class Swimmer:
    def swim(self):
        print("Swimming!")

# Define a base class that provides flying behavior
class Flyer:
    def fly(self):
        print("Flying!")

# Goose inherits both swimming and flying behavior
class Goose(Swimmer, Flyer):
    pass

# Create a Goose instance and call methods from both base classes
my_goose = Goose()
my_goose.swim() 
my_goose.fly()  
