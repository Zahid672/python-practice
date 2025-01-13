class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        
    def printname(self):
        print(self.fname, self.lname)
        
        
## use the Person class to create an object, and then execute the printname method:

p1 = Person("Saeed", "Ahmad")
p1.printname()

## To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class
## create a class named Student, which will inherit the properties and methods from the Person class
class Student(Person):
    pass

## use the pass keyword when you do not want to add any other properties or methods to the class

x = Student("Khan", "Umar")
x.printname()

## Now the Student class has the same properties and methods as the Person Class
