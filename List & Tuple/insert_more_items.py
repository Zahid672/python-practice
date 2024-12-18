# If we insert more items than we replace, the new items will be inserted where we specified, and the remaining items will move accordingly.

mylist = ["apple", "banana", "cherry"]

mylist[1:2] = ["mango", "peach"]

print(mylist)