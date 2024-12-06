### The following example shows how to use a default parameter value. If we call the function without argument, it uses the default value:

def identity(my_country = "Qatar"):
    print("my country is: " + my_country)
    
    
identity("India")
identity("Afghanistan")
identity()

identity("USA")