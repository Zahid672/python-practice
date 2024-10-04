####Functions in Python: Block of statements that perform a specific task. Functions are used for reducing redundancy
## def func_name(parameter1, parameter2...): Function Defintion. Moreover, parameter1, and parameter2 are variables names.
##some work
## return value
## function_name(arg1, arg2...)#function call. Moreover, when we assign the values then we call that arguments..

def calc_sum(a, b):
    sum = a + b
    print(sum)
    return calc_sum

calc_sum(4, 5)
calc_sum(45, 65)
calc_sum(46, 57)
calc_sum(45, 65)


## function definition
def calc_sum(c, d): # (c, d --- > parameters)
    return c + d

sum = calc_sum(8, 4) # function call; (8, 4 ... > arguments)
print(sum)


def print_hello():
    print("hello")

print_hello()


### two things are completely optional in functions (first, if you do not want to provide parameter to the function e.g. in the above example 'print_hello()'. Second, if you do not want your function to return a value means not taking any input(parameter), e.g. in 'print_hello' function)
