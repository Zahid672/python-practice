## example 1
def my_function(x, /):
    """To specify that a function can have only positional arguments,
    
    add ', /' after parameters"""
    print(x)
    
my_function(4)

## example two
def multi_arguments(h, w, /):
    print(h, w)
    
multi_arguments(7, 8)


## example 1
def kwordarguments(x, y):
    """without the ', /' you are actually allowed to use keyword arguments even if the function expects positional arguments.
    
    However when adding ', /' you will get an error if you try to send a keyword argument."""
    print(x, y)
    
kwordarguments(x = 55, y = 66)