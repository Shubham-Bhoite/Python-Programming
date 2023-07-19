#Exception handling is the process of responding to unwanted or unexpected events when a computer program runs.
# Used to deal with Errors

try:
    num = int(input("Enter an integer: "))
    a = [11, 45]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
    
except IndexError:
  print("Index Error")
# We Can USe Multiple Except Statements