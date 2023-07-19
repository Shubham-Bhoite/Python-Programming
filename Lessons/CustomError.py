# We can produce custom error in python

s=int(input("Enter any value between 20 to 35: "))

if(s<20 or s>35):
    raise ValueError("This sentence is a lie!!! Enter Number Between 10 to 20")
else:
    print("You are the smart yahh!!!")