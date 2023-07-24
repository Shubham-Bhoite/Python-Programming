# Type of method that is bound to the class and not the instance of class

# Type of method that is bound to the class and not the instance of class

class country_Data:
    states="Maharashtra"
    def personName(self):
        print(f"My name is {self.name} and I lived  in {self.states}")
    
    @classmethod
    def changeState(cls,NewState):
        cls.states=NewState

person1=country_Data()
person1.name="Shubham"
person1.personName()

person2=country_Data()
person2.name="Akshay"
person2.changeState("Delhi")
person2.personName()

print(country_Data.states) # states Changed For Other Instances too

person3=country_Data()
person3.name="Rahul"
person3.personName()