## An iterator is an object that contains a countable number of values. 
## An iterator is an object that can be iterated upon, meaning that we can traverse through all the values.
## an iterator is an object which implements the iterator protocol, which consist of the method __iter__() and __next__().

## lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which we can get an iterator from.
## All these objects have a iter() method which is used to get an iterator:

## Example: return an iterator from a tuple, and print each value.

mytuple = ("apple", "banana", "grape")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

### Every strings are iterable objects, and can return an iterator

mystr = 'banana'
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))