# Special Method in a class used to create and initialize an object of a class
# Constructor is invoked automatically when an object is created
#syntax==>  def __init__(self):
 
# Types: 1) Default 2)Parameterized

#1) Parameterized constructor:
class Details:
    def __init__(self, birds, group):
        self.birds = birds
        self.group = group

obj1 = Details("Sparrow", "birds")
print(obj1.birds, "belongs to the", obj1.group, "group.")


#2) Default constructor:
class info:
  def __init__(self):
    print("Hello! Shubham, How are You?")
obj1=info()