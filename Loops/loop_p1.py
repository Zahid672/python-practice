"""
Problem statement: Print all prime numbers between 1 and 100

Step-wise solution:
- 
- 
- 

"""


start = 1
last = 100

print("Prime number between", start, "and ", last, "are:")

for num in range(start, last+1):
    if num > 1:
        for i in range(2, num):
            if(num % i) == 0:
                break
        else:
            print(num)


"""Print the first 10 natural numbers using a while loop."""
i = 0

while i <= 9:
    i += 1
    print("The first 10 natural numbers are:", i)



### Print all even numbers between 1 and 20 using a while loop.

num = 1
while num <= 20:
    num += 1
    if(num % 2 == 0):
        print(num)




#### Calculate the sum of numbers from 1 to a given number n using a for loop.

# list = [1, 2, 3, 4, 5, 6, 7, 8]

# for n in list:


#     i += 1
    

 #### Print a multiplication table for a given number using a for loop.

a = [1, 2, 3, 4, 5, 6, 7, 8]

for num in a:
    print("2 x ", num, "=", 2*num)
    num += 1

### Reverse a given number using a while loop.

z = 6
while z >= 1:
    z -= 1
    print(z)





#### Calculate the factorial of a given number using a while loop.

fc = 6
while fc >= 1:
    fc -= 1
    print(fc*i)


    ### Print a pattern of stars in increasing order:




####Calculate the average of numbers in a list using a for loop.

lst = [ 1, 4, 5, 6, 7, 3]

sum = 0

for num in lst:
    sum += num
    average = sum / len(lst)
    print(average)

    






        
    

    