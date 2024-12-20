## the pop method removes the specified index
mylist = ["banana", "fruit", "apple"]
mylist.pop(1)
print(mylist)

## if we do not specify the index, the pop() method removes the last item.
mylist1 = ["jan", "khan", "malik"]
mylist1.pop()


## the del keyword also removes the specified index

mylist2 = ["Hello", "Hi", "Welcome"]
del mylist2[0]
print(mylist2)

### The del keyword can also delete the list completely.

mylist3 = ["Hello", "Hi", "Welcome"]

del mylist3
print(mylist3)