#### Given an integer, , perform the following conditional actions:

## 1- If n is odd, print Weird
## 2- if n is even and in the inclusive range of 2 to 5. print Not Weird
## 3- if n is even and in the inclusive range of 6 to 20. print Weird
## 4. if n is even and greater than 20. print Not Weird

n = 78
if(n % 2 != 0):
    print("Weird")
    
elif(n % 2 == 0 and 2 <= n <= 5):
    print("Not Weird")
    
elif(n % 2 == 0 and 6 <= n <= 20):
    print("Weird")
    
elif(n % 2 == 0 and n > 20):
    print("Not Weird")
    
    
    
## using function

def condstatements(n):
    if(n % 2 != 0):
        print("Weird")
    
    elif(n % 2 == 0 and 2 <= n <= 5):
        print("Not Weird")
    
    elif(n % 2 == 0 and 6 <= n <= 20):
        print("Weird")
    
    elif(n % 2 == 0 and n > 20):
        print("Not Weird")
        
condstatements(n)
    