### can use these two concepts together in a single function, but we must be careful to specify positional parameters before keyword arguments.
##Also, parameters that are to gather up any remaining arguments go at the end in the same order: 
###positional first and then keywords. In big applications, it’s best to avoid mixing keyword and positional arguments. 

def collect_args(b, e, a = 432, c = 333, *args, **kwargs):
    print(a, b, c, e)
    print(args)
    print(kwargs)
    print(args)
    
collect_args(555, 88, 432, 512, 767, 887, 564, first = 729, second = 445, third = 8858)
