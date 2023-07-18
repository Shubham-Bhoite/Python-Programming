# Operations On Sets
states1={"Maharashtra","Goa","Gujrat","Kerala","Bihar"}
states2={"Tamilnadu","Delhi","Punjab","Jammu","Goa","Kerala"}

#Union 
print("Union Set: ",states1.union(states2)) #print values of both set excepting Duplicate values

# Intersection
print("Intersection Set: ",states1.intersection(states2)) # Print Common Values

# Symmetric Difference
print("Symmetric Difference: ",states1.symmetric_difference(states2)) # not similar in both sets

# Difference 
print("Difference: ",states1.difference(states2))


# Methods In Sets

# isdisjoint()
print("Is Disjoint: ",states1.isdisjoint(states2))

# issuperset()
print("Is Super Set: ",states1.issuperset(states2))

# issubset()
print("Is Sub Set: ",states1.issubset(states2))

# Add Single item to set
states1.add("Tripura")
print("Added Single Element: ",states1)

# Add More Then One item
newSet={"Assam","Karnataka"}
states2.update(newSet)
print("Added Multiple Element: ",states2)

# Remove From Set with remove()
states2.remove("Goa")
print("Removed Single Element: ",states2) #If Item Not found It will throw error

# Remove From Set with discard()
states2.discard("Jammu")
print("Removed Single Element: ",states2) #If Item Not found It will not throw error


# Del keyword to delete set
delemoji={"happy", "sad","angry"}
del delemoji
# print(delSet) # Throws an Error

#Use To delete all item in sets
clearSet={51,62,73,84,95,41}
clearSet.clear()
print(clearSet)

#Check if Element is present or Not
if 84 in clearSet:
    print("Yes")
else:               #This will print No because we cleared Set in previous method(Line 55)
    print("No")