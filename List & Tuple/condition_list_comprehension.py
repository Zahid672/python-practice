## The condition is like a filter that only accepts the items that valuate to true

mylist = ["apple", "banana", "cherry", "orange"]

newlist = [items for items in mylist if items != "banana"] 

print(newlist)