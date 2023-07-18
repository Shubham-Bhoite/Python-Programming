#Function call itself called recursion.

# factorial(7) = 7*6*4*4*3*2*1
# factorial(6) = 6*4*4*3*2*1
# factorial(4) = 4*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(0) = 1

#Factorial Program

def factorial(num):
    if(num==0 or num==1):
        return 1
    else:
        return num*factorial(num-1)  # Recursion is Used 
    
print(factorial(4))
# 4 * factorial(3)
# 4 * 3 * factorial(2)
# 4 * 3 * 2 * factorial(1)
# 4 * 3 * 2 * 1