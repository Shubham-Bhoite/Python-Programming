# Finally is used to run block of code after try catch block
# It used in functions

s=int(input("Enter one Number :"))
s1=int(input("Enter another Number :"))

try:
    print("Addition of Numbers is",s+s1)
except:
    print("Enter Non zero Number!!!")
finally:
    print("I am always for you!!!")

# Finally will run after running or using return function 
def alpha(a,b):
    try:
        print(f"{a}*{b} :",a*b)
        return 1
    except:
        print("my pleasure!!")
        return 0
    finally:
        print("Hey Dear, I always for you!!")

s=int(input("Enter a: "))
s1=int(input("Enter b: "))
x=alpha(s,s1)
print(x)
