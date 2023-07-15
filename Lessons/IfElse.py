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