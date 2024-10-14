### when one class (child/derived) derives the properties & methods of another class(parent/base). For example:
## class Car:
##      ...
## class ToyotaCar(Car):
##      ...



## Types of Inheritance: There are three types of inheritance. 1- Single inheritance 2. Multi-level inheritance 3. Multiple inheritance
##### 1- Single inheritance
class Car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name
        

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.name)
print(car1.start())

## Types of Inheritance: There are three types of inheritance. 1- Single inheritance 2. Multi-level inheritance 3. Multiple inheritance