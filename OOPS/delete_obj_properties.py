## object properties can be deleted using del keyword
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def myfunc(self):
        print("Hello my age is " + self.age)
        
p1 = Person("Khan", 99)

del p1.age 
print(p1.age)