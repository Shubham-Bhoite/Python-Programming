# Local Variables are accessible into only particular function
# Global Variable can be accessed from anywhere

#Global Variable
y=50
def my_func():
    x=20   #Local Variable
    print(x)
my_func()
#print(x)  # This will throw error


#How to change global variable from function
change=100
def change():
    global char
    char=70
change()
print(char) # This Will Print Changed Value
