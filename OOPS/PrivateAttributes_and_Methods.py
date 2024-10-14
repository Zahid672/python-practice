### Private attributes & methods are meant to be used only within the class and not accessible from outside the class.
class Person:
    __name = "anonymous"

    def __hello(self):
        print("hello person")

    def welcome(self):
        self.__hello()


p1 = Person()
print(p1.welcome())