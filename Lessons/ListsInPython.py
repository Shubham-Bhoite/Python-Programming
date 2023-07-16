# Lists Are Collection Of Data Items 
# Contain any type of data type

myList=[1,2,3,4,"Sandip",8.2,True]
print(myList)

#positive Indexing
print(myList[4])

#Negative Indexing
print(myList[-4])

# Check whether element is present or not
if 4 in myList:
    print("Yes")
else:
    print("No")


#List Slicing
print(myList[1:4])
print(myList[-3:-1])

#Jump index   
print(myList[0:6:2])