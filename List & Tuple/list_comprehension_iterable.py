## The iterable can be any iterable object, like a list, tuple, set etc

mylist = [item for item in range(5)]
print(mylist)

mylist1 = [item for item in range(6) if item < 4]
print(mylist1)