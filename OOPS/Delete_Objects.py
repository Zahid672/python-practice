class Person:
    def __init__(self, name, age):
        self.name = name 
        
        self.age = age
        
    def myfunc(self):
        print("my name is " + self.name)
        
p1 = Person("Saeed", 33)

del p1

print(p1)