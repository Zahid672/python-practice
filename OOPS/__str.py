### Example: The string representation of an object without the __str__() function.
class Person:
    """The __str__() function control what should be returned
    when the class object is represented as a string. If the __str__() function is not set, the string representation of the object is returned.
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
p1 = Person("Zahid", 36)
    
print(p1)


### Example: The string representation of an object WITH the __str__() function:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name}({self.age})"
    
p1 = Person("Saeed ", 24)
print(p1)
        
    
    
    