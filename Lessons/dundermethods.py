class Employee:

#The __init__ method is a special method that is automatically invoked when you create a new instance of a class.
#this method is also called as constructor.
  def __init__(self, name):
    self.name = name


#The __len__ method is used to get the length of an object.
#This is useful when you want to be able to find the size of a data structure, such as a list or dictionary.
  def __len__(self):
    i = 0
    for c in self.name:
      i = i + 1
    return i

#The __str__ methods are used to convert an object to a string representation.
#The str method is used when you want to print out an object.
  def __str__(self):
    return f"The name of the employee is {self.name} str"
    
    
#The __repr__ methods are used to convert an object to a string representation.    
#repr method is used when you want to get a string representation of an object that can be used to recreate the object.
  def __repr__(self):
    return f"Employee('{self.name}')"

#The __call__ method is used to make an object callable.
#you can pass it as a parameter to a function and it will be executed.
  def __call__(self):
    print("Hey I am good")


e = Employee("Shubham")
print(str(e))
print(repr(e))
print(e.name)
print(len(e))
e()