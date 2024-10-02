### For loops are used for sequential traversing. e.g. For traversing different datatypes e.g. list, string, tuples etc.
##Regarding while loop, agar hamain kisi iterator k ooper kaam karna ha e.g. 
## agar hamaray pass koi variable ha jis ki value ko hum update kar rahay ha aur hamaray pass koi stopping condition ha. 
# #tu yeh saaray kaam ham WHILE LOOP se kartay ha.

list = [1, 2, 3]

for element in list:  ## 'for' is keyword. 'element' is variable. 'in' is keyworkd. 'list' is variable name. one by one the values of variable 'list' goes into 'element' variable.
    print(element)

#################
nums = [5, 4, 3, 2, 1]

for value in nums:
    print(value)
else:
    print('end')

    #########################

veggies = ['potato', 'salad', 'spinach', 'cauli flower']

for vegetable in veggies:
    print(vegetable)



######################

tup = (8, 4, 3, 2)

for values in tup:
    print(values)


####################
str = 'God help those, those who help themselves'

for charac in str:
    if(charac == 's'):
        print("s found")
        break
    print(charac)
else:
    print("END")


    ###############

### print the elements of the following list using a loop.

list = [1, 4, 9, 16, 25, 36, 49, 64, 81]

for elements in list:
    if(elements == 25):
        print("found 25")
        break
else:
    print(list)

    #### search for a number x in tuple using for loop

l = (1, 4, 9, 16, 25, 36, 49, 64)

for el in l:
    if(el == 16):
        print("number found:", el)    
        break


#### write a program to add n natural numbers
n = 5
sum = 0

for i in range(1, n+1):
    sum += i
    
    
print("total sum", sum)


## write a program to find the factorial of n numbers

n = 5
fact = 1
i = 1 

while i <= n:
    fact *= i
    i += 1

print("total sum = ", fact)