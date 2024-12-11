class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
        def my_func(self):
            print("Hello my name is " + self.name)
            
p1 = Person("Zahid", 55)

p1.age = 77
print(p1.age)