# By Using Enumerate Function we can extract index of list

marks=[10,12,34,56,88,99,13]

for index,mark in enumerate(marks):
    print(mark)
    if(index==5):
        print("You are Smart!!!")


marks = [12, 56, 32, 98, 12,  45, 1, 4]

for index, mark in enumerate(marks, start=1):
  print(mark)
  if(index == 3):
    print("Hello, Shubham!")
    


# Loop over a tuple and print the index and value of each element
colors = ('red', 'green', 'blue')
for index, color in enumerate(colors):
    print(index, color)


# Loop over a string and print the index and value of each character
s = 'hello'
for index, c in enumerate(s):
    print(index, c)

    
    

