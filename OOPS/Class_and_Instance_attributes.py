class Student:
    college_name = "Mardan Model" ### class attribute

    def __init__(self, name, marks):
        self.name = name ### object attribute
        self.marks = marks
        print("adding new student in Database..")

s1 = Student("Zahid", 99)
print(s1.name, s1.marks)

s2 = Student("Saeed", 100)
print(s2.name, s2.marks)

s3 = Student("Imran", 100)
print(s3.name,s3.marks)

print(s3.college_name)


####### when there is same name attribute (variable name) in class and object, then the precedence (priority or preference) of object attribute is higher than class attribute. For example:
class Student:
    college_name = "MMS&C" 
    name = "ananymous"  ### class attribute

    def __init__(self, name, marks):
        self.name = name ### object attribute (In the output we will get this output name, object attribute > class atrribute)
        self.marks = marks
        print("adding new student..")

s1 = Student("Khan", 88)
print(s1.name, s1.marks)

