### OOPS: There are generally 4 pillars of OOPS. i. Abstraction ii. Encapsulation iii. Inheritance iv. Polymorphism
### Abstraction: Hiding the implementation details of a class and only showing the essential features to the user.


class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True  ### unnecessary details are hiding
        self.acc = True
        print("Car started..")

car1 = Car() ### show only the essential things
car1.start()