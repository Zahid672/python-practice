class Person:
    """Objects can also contain methods. Methods in objects are functions that belong to the object."""
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        
    def myfunc(self):
            print("Hello my name is " + self.name)
            
            
p1 = Person("Zahid", 50)

p1.myfunc()