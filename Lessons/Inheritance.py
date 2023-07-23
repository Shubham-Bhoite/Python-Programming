# One Class is derive from another class
# It Inherits all public and protected methods from parent class

#Syntax-->
# class BaseClass:
#   Body of base class
# class DerivedClass(BaseClass):
#   Body of derived class

#Example-->
class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id 

  def showDetails(self):
    print(f"The name of Employee: {self.id} is {self.name}")

class Programmer(Employee):
  def showLanguage(self):
    print("The default langauge is Python")


e1 = Employee("Arjun Kadam", 123)
e1.showDetails()
e2 = Programmer("Prashant Jagtap", 321)
e2.showDetails()
e2.showLanguage()
