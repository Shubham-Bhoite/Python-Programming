# Ordered Collection Of Element In Python
# Items are in key value pair

info={
    "Name":"Shubham",
    "Age":"21",
    "isDriveCar":"Yes",
    "isVoter":True,
}

print(info)

print(info["isDriveCar"]) #print particular item if not found throws error
print(info.get("Age")) #print particular item if not found does not throws error
print(info.keys()) #display all keys
print(info.values()) # display all Values
print(info.items()) # display all Key-Value Pairs



## Dictionary Methods ==>

#Update() method
info = {'name':'Shubham', 'age':21, 'Drive':True, 'isMarried':False}
print(info)
info.update({'DOB':2002})
print(info)

#Remove all items
#using Clear() method
info.clear()
print(info)

#using pop() method
info.pop('name')
print(info)

#using popitem()method==> Remove Last Item From Dictionary
info.popitem()
print(info)

#Delete Dictionary 
dic={
    "Shubham":"502",
    "Arjun":"434"
}
del dic["Shubham"] #delete particular key pair
print(dic)
del dic #delete all values