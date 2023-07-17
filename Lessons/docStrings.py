# Doc Strings Are written after function declaration and before function definition

def squares(num):

    '''This is Paragraph    #We can write any sentence if you want 
    Line 1 
    Line 2
    Line 3 '''
    print("Square is: ",num**2)

squares(15)

print(squares.__doc__) #this will print Doc-Strings
