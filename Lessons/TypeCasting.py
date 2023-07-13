# Type Casting Means Converting One Data Type Into Another.
# Implicit - Done By User or Programmer.
# Explicit - Done By Python (Convert Smaller Data Type to Higher Data Type)

x="3"
y="4"
print(x+y) #print string
print(int(x)+int(y)) #print int after type-casting


a=5
b=9.1
print(a+b)


### Example of Explicit typecasting ==>
string = "15"
number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum= number + string_number
print("The Sum of both the numbers is: ", sum)


### Example of Implicit typecasting ==> 
# Python automatically converts==> a to integer
a = 7
print(type(a))
 
# Python automatically converts==> b to float
b = 3.0
print(type(b))
 
# Python automatically converts==> c to float as it is a float addition
c = a + b
print(c)
print(type(c))