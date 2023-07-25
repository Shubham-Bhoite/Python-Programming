class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")
        
class Mammal:
    def __init__(self, name, body_color):
        self.name = name
        self.body_color = body_color
        
class Dog(Animal, Mammal):
    def __init__(self, name, breed, body_color):
        Animal.__init__(self, name, species="Dog")
        Mammal.__init__(self, name, body_color)
        self.breed = breed
        
    def make_sound(self):
        print("Bark!")
        
o  = Mammal("Shera", "Black")
print(o.name)
print(o.body_color)

print(Mammal.mro())