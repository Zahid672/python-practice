num1 = 0
num2 = 1

print("Fibonnaci sequence:")

for i in range(10):
    # print next number of a series
    
    # add last two numbers to get next number
    res = num1 + num2
    num1 = num2
    num2 = res
    print(num1, end=' ')
