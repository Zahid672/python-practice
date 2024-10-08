### __init__ function: also called constructor. All classes have a function called __init__(self), which is always executed when the object is being initiated.
## The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

class Student:
    def __init__(self, fullname, marks): ##parameterized constructor
        self.name = fullname
        self.marks = marks


s1 = Student("Imran", 88)
print(s1.name, s1.marks)

s2 = Student("Zahid", 66)
print(s2.name, s2.marks)




