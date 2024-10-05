## there are two types of functions. 1- Buitin Functions (already available in the language) 2- user defined functions (defined by the user)
## Default Parameters: Assigning a default value to parameter, which is used when no argument is passed. for example:
def calc_prod(a=1, b=1):
    print(a * b)
    return a * b

calc_prod()

## write a function to print the length of a list. (list is the parameter)
cities = ["Peshawar", "Mardan", "Timergara", "Mingora"]

def len_list(cities):
    print(len(cities))
    return len_list

len_list(cities)

## write a function to print the elements of a list in a single line. (list is the parameter)

def print_list(list):
    for item in list:
        print(item)

print_list(cities)


## write a function to find the factorial of n. (n is the parameter)
def calc_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

calc_fact(5)


### find factorial through FOR loop
n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)

### write a function to convert USD to INR
def converter(USD_val):
    inr_val = USD_val * 83
    print(USD_val, "USD =", inr_val, "INR")

converter(1)



              







