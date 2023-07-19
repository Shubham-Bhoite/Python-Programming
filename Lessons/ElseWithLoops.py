#We Can Use Else Within The Loops

#This Will Execute else after completing Loop
for i in  range(7):
    print(i)
else:
    print("there is no any loop")

#Else is not executed if we use Break in between loop
for s in range(9):
    print(s)
    if(s==5):
        break
else:
    ("there is no any loop")
