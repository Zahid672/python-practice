# If we insert more items than we replace, the new items will be inserted where we specified, and the remaining items will move accordingly.

mylist = ["apple", "banana", "cherry"]

mylist[1:2] = ["mango", "peach"]

print(mylist)

### if we insert less items than we replace, the new items will be inserted where we we specified, and the remaining items will move accordingly.

mynewlist = ["apple", "banana", "cherry"]
mynewlist[1:3] = ["orange"]

print(mynewlist)