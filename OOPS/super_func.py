## python also has a super() function that will make the child class inherit all the methods and properties from its parents
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lname = lname
        
        
    def printname(self):
        print(self.firstname, self.lname)
        
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        
        
x = Student("Imran", "Ullah")
x.printname()