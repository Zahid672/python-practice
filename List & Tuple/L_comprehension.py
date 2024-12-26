fruits = ["banana", "apple", "cherry"]

newlist = ['hello' for x in fruits]

print(newlist)

####

mylist = ["khan", "afghan", "russia"]
newlist = [item if item != "russia" else "uzbek" for item in mylist]

print(newlist)