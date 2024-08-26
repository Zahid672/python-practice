### Set is the collection of the unordered (means there is no index) items.
### Each element in the set must be unique & immutable. 
## we can store tuple, string, float, integer, boolean inside set. 
# ###But we cannot store List and dictionary inside Set. Because List and dictionary are mutable (changeable).

collection = {1, 2, 3, 4, 3, 2, 1}
print(collection)
print(type(collection))

collection = {1, 2, 3, 4, 3, 2, 1, "hello", "world"}
print(collection)


collection = {1, 2, 3, 4, 3, 2, 1, "hello", "world", "hello", "world"} # ignore repitition or duplicate value
print(collection)
print(len(collection))

collection = set()
collection.add(1)
collection.add(2)
collection.add("Apple")
collection.remove(1)
collection.clear()

print(len(collection))

Pop1 = {"Hello", "world", "how", "are"}
print(Pop1.pop())

U = {1,2,3}
U2 = {3,4,5}
print(U.union(U2))

print(U.intersection(U2))

### write a program that store following word meanings in a python dictionary:

dict = {"cat": "a small animal", 
        "table": ['a piece of furniture','list of facts figures']
        }
print(dict)

subjects = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
print(len(subjects))

### write a program to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.
marks = {}
sub1 = int(input("enter marks of maths"))
marks.update({"maths" : sub1})
sub2 = int(input("enter marks of eng"))
marks.update({"eng": sub2})
sub3 = int(input("enter marks of phy"))
marks.update({"phy": sub3})

print(marks)



