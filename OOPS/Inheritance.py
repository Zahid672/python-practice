## Inheritance allows us to define a class that inherits all the methods and properties from another class.
## Parent class is the class being inherited from, also the base class.
## Child class is the class that inherits from another class, also called derived class.



## Create a parent class: Any class can be a parent class, so the syntax is the same as creating any other class:
## create a class named Person, with firstname and lastname properties, and a printname method:

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        
    def printname(self):
        print(self.fname, self.lname)
        
        
## use the Person class to create an object, and then execute the printname method:

p1 = Person("Saeed", "Ahmad")
p1.printname()



        