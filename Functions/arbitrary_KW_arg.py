### If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:

### 1. Example
def my_function(**kids):
    print("His last name is: " + kids["lname"])
    
my_function(f_name = "Zahid", lname = "Ullah")

###2. Example
def collect_kwargs(**kwargs):
    print(kwargs)
    
collect_kwargs(one = 1, two = 2, three = 3)