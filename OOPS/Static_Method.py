## Methods that don't use the self parameter (work at class level)
### Decorator: allow us to wrap another function in order to extend the behaviour of the wraped function, without permanently modifying it.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    @staticmethod    #### decorator
    def hello():
        print("hello")



s1 = Student("Khan", 88)
print(s1.hello())
