##The self parameter is a reference to the current instance of the class and is used to access variables that belong to the class

class person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
    def myfunc(self):
        print("Hello my name is " + self.name)
        
p1 = person("Khan", 33)

p1.myfunc()