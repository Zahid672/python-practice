class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def myfunc(self):
        print("my name is " + self.name)
        
p1 = Person("Zahid", 77)

del p1.age

print(p1.age)