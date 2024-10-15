### A class method is bound to the class & receives the class as an implicit first argument.
### Note- static method can't access or modify class state & generally for utitility
class Person:
    name = "anonymous"

    def ChangeName(self, name):
        Person.name = name


p1 = Person()
p1.ChangeName("Zahid")
print(p1.name)
print(Person.name)


### instance methods wo ha jin k andar self as an argument aatta ha
## class methods wo ha jin k andar class first implicit argument aata ha 
### static methods wo ha jo class ya instance methods dono mai say kisi k attribute ya instance ko change ya access nai karta