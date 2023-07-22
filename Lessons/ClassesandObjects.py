class myinfo:
  name = "Shubham"
  occupation = "Web Developer"
  networth = 100
  def myinfo(self):
    print(f"{self.name} is a {self.occupation}")

a = myinfo()
b = myinfo()

a.name = "Prashant"
a.occupation = "Blockchain Developer"

# print(a.name, a.occupation)
a.myinfo()
b.myinfo()


# self parameter:  #-->The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
class Details:
    name = "komal"
    age = 21

    def desc(self):
        print("My name is", self.name, "and I'm", self.age, "years old.")

obj1 = Details()
obj1.desc()
 

