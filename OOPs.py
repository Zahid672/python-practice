""" procedural ---- > Functional ----- > OOPS... 
Class is a blueprint for creating objects."""

# creating class
# class Student:
#     name = "Zahid"

# # creating object(instance), object is also called instance of class.
# s1 = Student()
# print(s1.name)

# class Car:
#     color = "white" #parameters
#     brand = "tesla" 

# car1 = Car()
# print(car1.color)
# print(car1.brand)

"""__init__ Function (constructor) All classes have a function called
__init__(), which is always executed when the object is being initiated.
The __init__ function is executed when the object is created. """

class Student:
    def __init_(self): #this constructor is called default constructor
        pass

    def __init__(self, name, marks): # this constructor is called parameterized constructor
        self.name = name # The variables inside the class are called attribute.
        self.marks = marks
        print("adding new student in Database")

s1 = Student("Zahid", 55)
print(s1.name,s1.marks)

s2 = Student("Saeed", 66)
print(s1.name,s1.marks)

"""The .self parameter is a reference to the current instance of the class,
 and is used to access variables that belongs to the class"""


# Class and Instance Attributes
