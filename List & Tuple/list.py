"""Lists in Python: A builtin data type that stores set of values. 
It can store elements of different types (integer, float, string, etc.)"""
#lists are mutable while strings are not mutable
marks = [23.2, 12.5, 32, 122.3, 432.1]
print(marks)
marks[0] = [333.1]
print(marks)
print(marks[3:4])
print(marks[1])


student = ["Zahid", 40, "Afghanistan"]
print(student)
print(len(student))