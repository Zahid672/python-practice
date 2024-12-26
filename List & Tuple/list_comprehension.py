### list comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
### Example: Based on a list o fruits, if we want a new list, containing only the fruits with the letter "a" in the name.
## without list comprehension we will have to write a "for" statement with a conditional test inside.
# fruits = ["apple", "pineapple", "cherry"]
# newlist = []
# for items in fruits:
#     if "a" in items:
#         newlist.append(items)
        
# print(newlist)


### with list comprehension we can do all that with only one line of code

fruits = ["apple", "pineapple", "cherry"]

newlist = [items for items in fruits if "a" in items]

print(newlist)



        