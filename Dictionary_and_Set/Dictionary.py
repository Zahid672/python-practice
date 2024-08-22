## Dictionaries are used to store data values in key:value pairs. 
# #They are unordered (no index), mutable (changeable) & don't allow duplicate keys

dict = {"name": "Khan",
        "class": 4,
        "cgpa": 4.2,
        "marks": [44, 43, 36]}
print(dict)

print(dict["name"])
print(dict["cgpa"])
print(dict["marks"])

dict["name"] = "Saeed"
print(dict)

### nested dictionary
student = {
    "name": "Zahid",
    "subjects": {
        "OOPS": 88,
        "python": 99,
        "Maths": 55
    }
}
print(student)

print(student["name"])
print(student["subjects"])

print(student["subjects"]["python"])

### Dictionary Methods

myDict = {"name": "Zahid",
          "age": 44,
          "village": "null"}
print(myDict.keys()) ## returns all keys
print(len(myDict))   
print(list(myDict.keys())) 

print(myDict.values()) ## returns all values
print(list(myDict.values())) ### type cast

print(myDict.items()) #### returns all (key, val) pairs as tuples
print(list(myDict.items()))
pair = list(myDict.items())
print(pair[0])

myDict.update({"City": "Peshawar"}) ### inserts the specified items to the dictionary
print(myDict)




