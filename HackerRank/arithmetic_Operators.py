### The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

##The first line contains the sum of the two numbers.
##The second line contains the difference of the two numbers (first - second).
##The third line contains the product of the two numbers.

a = 3
b = 5

c = a + b
print(c)

d = a - b
print(d)

e = a * b
print(a+b, a-b, a*b)



def ArithOper(n1, n2):
    print(n1 + n2)
    print(n1 - n2)
    print(n1 * n2)



if __name__ == '__main__':
    a = int(input(3))
    b = int(input(5))
    
    ArithOper(a, b)