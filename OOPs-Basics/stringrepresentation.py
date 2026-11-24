class Cereal():
    def __init__(self,name,brand,fiber):
        self.x=name
        self.y=brand
        self.z=fiber
    
    def __str__(self):
        return "{} cereal is produced by {} and has {} grams of fiber in every serving!".format(self.x,self.y,self.z)

c1=Cereal("Corn Flakes","Kellogg's",2)
c2=Cereal("Honey Nut Cheerios","General Mills",3)

print(c1)
print(c2)