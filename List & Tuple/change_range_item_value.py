"""To change the value of items within a specific range, define a list with the new values, 
and refer to the range of index numbers where we want to insert the new values."""

mylist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
mylist[0:3] = ["pineapple", "mango", "potato"]

print(mylist)