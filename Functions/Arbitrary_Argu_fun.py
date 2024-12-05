### If you do not know how many arguments that will be passed into your function, 
# ##add a * before the parameter name in the function definition. 
##This way the function will receive a tuple of arguments, and can access the items accordingly:
### 1.
def my_function(*kids):
    print("The youngest child is: " + kids[1])
    
    
my_function("Javed", "Shah", "Fahad")


### 2.
def countries_capital(*args):
    print("The capital of India is: " + args[0])
    
countries_capital("Dehli", "Seoul", "Kabul")

### 3. 
def collect_args(*args):
    print (args)
    
collect_args("History", "Justice", "Cruelty")


