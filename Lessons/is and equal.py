# "is" and "==" are both comparison operators.
# "is" used to compare location of object in memory
# "==" used to compare value of an objects
# "is" Shows True if object is not changeable(tuples,etc)

print("For Lists: ")
lst1=[1,2,3,4,5]
lst2=[1,2,3,4,5]

print("Is Memory Location Same: ",lst1 is lst2)
print("Are Values Same: ",lst1 == lst2)

print("\nFor Tuples: ")
tup1=(1,2,3,4,5)
tup2=(1,2,3,4,5)

print("Is Memory Location Same: ",tup1 is tup2) 
print("Are Values Same: ",tup1 == tup2)
