## The ___init__() is called automatically every time the class is being used to create a new object.
## When we add the __init__function, the child class will no longer inherit the parent's __init__function().
## To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        
    def printname(self):
        print(self.firstname, self.lastname)
        
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        
x = Student("Afghan", "khan")
x.printname()