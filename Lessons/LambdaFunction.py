# Lambda Functions is a small anonymous function without a name

int= lambda float:float*2
print(int(5))

# we can pass function as an argument to another function
def my_fun(name,value):
    print(10+name(value))

my_fun(lambda float:float*float,4) # Here We Have Passed Lambda Function as an argument 



# MAP Function
# The map Function applies a function to each element in sequence & returns a new sequence containing transformed elements

my_list=[1,2,3,4,5,6,7,8,9,10]
cube=map(lambda int:int*int*int,my_list)
print(tuple(cube))


# Filter Function
# The filter function filters a sequence of element based on give predicate and returns a new sequence containing only the element that meet the predicate
filterlist=list(filter(lambda int:int>5,my_list))
print(filterlist)

# Reduce Function
# Function takes two arguments and returns a single value
from functools import reduce
multivalue= reduce(lambda x,y:x+y,my_list)
print(multivalue)