#####Private attributes & methods: Private attributes and methods are meant to be used only within the class and are not accessible from outside the class.
### for example: the below example is public class, because everything inside the class can be accessed from outside the class.
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Zahid")
print(s1.name)

### On the other hand there are some sensitive informations (attributes, methods) which we want to keep private. we don't want give access from outside the class. 
# For example:

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

acc1 = Account("1343", "zuye")
print(acc1.__acc_pass) ### Now this become private and we cannot access from outside class.