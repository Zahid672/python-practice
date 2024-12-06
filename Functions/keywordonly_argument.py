def keyword_only_argument(*, x):
    """To specify that a function can have only keyword arguments,
    
    add *, before the arguments"""
    
    print(x)
    
keyword_only_argument(x= 3)


## example 2
def without_asterisk(x):
    """you are allowed to use positional arguments even if the 
    
    function expect keyword arguments. But with the *, you will get an error if you try to send a positional argument"""
    print(x)
    
without_asterisk(4)