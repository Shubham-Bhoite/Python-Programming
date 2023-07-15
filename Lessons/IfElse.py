#If Else
car=int(input("Enter Your Car Count : "))
if(car>=3):
    print("Congratulation! You can Purchase more Cars")
    if(car>5):
     print("You are Rich Person")
     
else:
    print("Sorry!! You cannot Purchase More Cars\n")
    
    
#elif

myInput=int(input("Enter Any Number: "))
if(myInput<0):
    print("The Number is Negative")
elif(myInput==0):
    print("The Number is Zero")
else:
    print("Number is Positive")
    
    
#Nested if Statements

num = 8
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    else:
        print("Number is greater than 11")
else:
    print("Number is zero")