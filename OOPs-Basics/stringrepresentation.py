class Cereal():
    # Initialize the cereal name, brand, and fiber amount
    def __init__(self,name,brand,fiber):
        self.x=name
        self.y=brand
        self.z=fiber
    
    # Return a readable string representation for a Cereal object
    def __str__(self):
        return "{} cereal is produced by {} and has {} grams of fiber in every serving!".format(self.x,self.y,self.z)

# Create two Cereal objects with their details
c1=Cereal("Corn Flakes","Kellogg's",2)
c2=Cereal("Honey Nut Cheerios","General Mills",3)

# Print each object's string representation
print(c1)
print(c2)