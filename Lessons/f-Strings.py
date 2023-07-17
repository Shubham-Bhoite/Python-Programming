# f-Strings Are Used to manipulate the strings in python

#Before f-strings
intro="Hello My Name is {} and I am From {}"
name="Shubham"
country="India"
print(intro.format(name,country)) # Right 
print(intro.format(country,name)) #Wrong


#after f-Strings
company="TCS"
Role="SDE"
myIntro=f"Hey Everybody, I got placed in {company} for {Role}"
print(myIntro)

print(f"{5*9}") #data type is String

#printing as it is f-strings
self=f"Hi!!! There I am {{name}}"
print(self)
