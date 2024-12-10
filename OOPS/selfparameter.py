class Person:
    """The self parameter is a reference to the current instance of the class, 
    and is used to access variables that belong to the class."""
    
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        
    def my_func(self):
        print("Hello my name is " + self.name)
        
h1 = Person("Zahid", 99)
h1.my_func()