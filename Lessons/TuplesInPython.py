#Tuples are similar to lists but tuples are not change.
#Tuples are Immutable.

Tuple1=(5,2,7,9,1,6,5,9,0,2)
print(Tuple1)
Tuple2=("Shubham",9.1, True, 15)
print(Tuple2)
Tuple3=(3,)
print(Tuple3)

#It Has Same Indexing operation like Lists

#indirect way to change Tuple

originalTuple=(11,22,33,44,55)
tempList=list(originalTuple) #convert tuple to List
tempList.append(66)          #modify List

originalTuple=tuple(tempList) #Convert List into Tuple
print(tempList)


#concatenate two Tuples
mytup1=("Shubham ")
mytup2=("Bhoite")
names=mytup1+mytup2
print(names)



#Tuple Methods

#Gives the count of given value
print(Tuple1.count(5))

#index of given value
print(Tuple1.index(7))
