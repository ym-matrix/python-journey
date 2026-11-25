class Swimmer:
    def swim(self):
        print("Swimming!")

class Flyer:
    def fly(self):
        print("Flying!")

class Goose(Swimmer, Flyer):
    pass

my_goose = Goose()
my_goose.swim() 
my_goose.fly()  
