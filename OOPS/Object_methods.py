## Objects can also contain methods. Methods in objects are functions that belong to the object.

### Question: Insert a function that prints a greeting, and execute it on the p1 object

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
    def myfunc(self):
        print("Hello my name is " + self.name)
        
        
p1 = Person("Khan", 55)

p1.myfunc()
    