
myList=[5,6,3,9,11,34,95,4,7,2,10,15,88,44]
print(myList)

#sorting The List in Ascending
myList.sort()
print(myList)
#sorting The List in descending
myList.sort(reverse=True)
print(myList)

#reverse the list
myList.reverse()
print(myList)

#Add new element at the end
myList.append(1)
print(myList)


#Print given index of given element
ind=myList.index(7)
print(ind)

#Occurrence of any element
occ=myList.count(11)
print(occ)

#copying List
List2=[21,22,23,24,25]
copiedList=List2.copy()
copiedList[0]=40
print(copiedList)

#list Inserting at given index 
#It does not change element but insert at that index
List3=[60,70,80,90,100]
print(List3)
List3.insert(99,101)
print(List3)
