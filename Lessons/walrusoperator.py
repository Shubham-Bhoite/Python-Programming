# walrus operator denoted by (:=)
#Walrus Operator reduce the code duplication.


#Without Walrus Operator==>
Animals = list()
while True:
 animal = input("What animal do you like?: ")
 if animal == "stop":
           break
Animals.append(animal)


# #With Walrus Operator==>
Animals = list()
while (animal := input("What animal do you like?: ")) != "stop":
    Animals.append(animal)
    
    
#Walrus Operator in a while loop:
numbers = [1, 2, 3, 4, 5]

while (n := len(numbers)) > 0:
    print(numbers.pop())
    
#Walrus Operator in an if statement:
names = ["Shubham", "Vaishnavi", "Rohan"]

if (name := input("Enter a name: ")) in names:
    print(f"Hello, {name}!")
else:
    print("Name not found.")