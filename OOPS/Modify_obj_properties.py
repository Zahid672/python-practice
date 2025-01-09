class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def myfunc(self):
        print("Hello my name is " + self.name)
        
        
p1 = Person("Zahid", 88)
p1.name = "Saeed"
print(p1.name)
        
        