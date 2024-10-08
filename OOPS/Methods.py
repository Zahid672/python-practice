## class is a collection of 2 things, i) Data (Attributes or properties) ii) Methods (functions). Methods are functions that belong to objects.
## the functions which written inside class is called methods

class Student:
    college_name = "MMS"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("welcome student")

s1 = Student("Zahid", 66)
s1.welcome()

##########
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("welcom student")
    def get_marks(self):
        return self.marks
    

s1 = Student("Zahid", 55)
print(s1.get_marks())