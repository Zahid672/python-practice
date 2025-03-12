#Enter Python code here and hit the Run button. 
# Given two integer numbers, write a Python code to return their product only if the product 
#is equal to or lower than 1000. Otherwise, return their sum.


def multi_sum(a, b):
    c = a * b
    if c <= 1000:
        return c
    else:
        a + b
        
        
result = multi_sum(20, 30)
print("The result is", result)


result1 = multi_sum(40, 30)
print("The result is", result1)