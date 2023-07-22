# Python decorators are powerful and versatile tool that allows you to modify the behavior of functions and methods
# It takes another function as an arguments

def begineer(fx):

    def newFun(*a,**b):
     print(" Thanks for visiting my profile!!")
     fx(*a,**b)
    return newFun

@begineer
def addfunction(a,b):
    print("The Addition is:", a+b)

addfunction(5,4)



#Example2==>

def greet(fx):
    def mfx(*args, **kwargs):
     print("Good Morning")
     fx(*args, **kwargs)
     print("Thanks for using this function")
    return mfx

@greet
def hello():
  print("Hello world")

@greet
def add(a, b):
  print(a+b)
  
# greet(hello)()
hello()
# greet(add)(1, 2)
add(1, 2)

