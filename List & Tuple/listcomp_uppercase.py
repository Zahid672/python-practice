## The expression is the current item in the iteration, but it is also the outcome, which we can manipulate before
### it ends up like a list item in the new list

fruits = ["apple", "banana"]
newlist = [x.upper() for x in fruits]
print(newlist)