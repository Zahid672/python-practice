## We can also use a for loop to iterate through an iterable object.

## Example: Iterate through the values of a tuple

mytuple = ("apple", "pomegr", "peach")

for item in mytuple:
    print(item)
    
    

### Iterate the characters of a string

mystr = "apple"

for str in mystr:
    print(str)

## the for loop actually creates an iterator object and executes the next() method for each loop.