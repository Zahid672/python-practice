## The __str__() function controls what should be returned when the class object is represented as a string.
## if the __str__() is not set, the string representation of the object is returned

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name}({self.age})"
    
p1 = Person("Khan", 44)
print(p1)