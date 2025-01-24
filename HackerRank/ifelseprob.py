## Given an integer, , perform the following conditional actions:

##If n is odd, print Weird
##If  n is even and in the inclusive range of 2 to 5, print Not Weird
## If n is even and in the inclusive range of 6 to 20 , print Weird
## If n is even and greater than 20, print Not Weird
## constraints 1 <= n <= 100


if __name__ == '__main__':
    n = int(input().strip())
    
    """
    1. if n is not divisible by 2--- > Weird. if condition
    2. if n is divisible by 2 and lies in range 2 to 5 print Not Weird. elif condition
    3. if n is divisible by 2 and lies in range 6 to 20 print Weird. elif condition
    4. If n is divisible by 2 and n is greater than 20, print Not Weird. elif condition
    """
    if n % 2 == 1:
        print("Weird")

    elif n % 2 == 0 and n in range(2, 5):
        print("Not Weird")

    elif n % 2 == 0 and n in range(6, 20):
        print("Weird")

    elif n % 2 == 0 and n > 20:
        print("Not Weird")