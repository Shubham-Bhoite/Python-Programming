myString="hey there I am shubham bhoite !!!!!"

print(myString.upper()) #convert to upper case 
print(myString.lower()) #convert to lower case 
print(myString.rstrip("!")) #removes the special type of symbols that we specified 

print(myString.replace("shubham","varad")) #replace the string 

print(myString.split(" ")) #split according to argument and make list

print(myString.capitalize()) #capitalize first letter

print(myString.title()) #capitalize first letter of all words

print(myString.swapcase()) #Swap the Cases

print(myString.find("s"))

print(myString.index("b"))

print(myString.isspace()) #check all string is of white spaces or not


str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("ishh"))
# print(str1.index("ishh"))

str1 = "WelcomeToTheConsole"
print(str1.isalnum())
str1 = "Welcome"
print(str1.isalpha())

str1 = "hello world"
print(str1.islower())

str1 = "We wish you a Very Happy Birthday"
print(str1.isprintable())
str1 = "         "       #using Spacebar
print(str1.isspace())
str2 = "  "       #using Tab
print(str2.isspace())

str1 = "World Vision India" 
print(str1.istitle())

str1 = "Python is a high level programming Language" 
print(str1.startswith("Python"))

str1 = "Python is a high level programming Language" 
print(str1.swapcase())

str1 = "His name is Rahul. Rahul is an honest man."
print(str1.title())