# base class

class Animal():
    def animal(self):
        print("I'm an Animal")    

# child class 1
class Cat(Animal):
    def cat(self):
        print("I'm a cat Meow Meow!")

# child class 2        
class Dog(Animal):
    def dog(self):
        print("I'm a dog Brak Bark!")

# create object of child classes
cat = Cat()
dog = Dog()

print("Cat")
cat.animal()
cat.cat()

print("\nDog")
dog.animal()
dog.dog()  
