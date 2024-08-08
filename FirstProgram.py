# First Program
print("Hello World")

# Python Character Set
"""Letters - A to Z, a to z
Digits- 0 to 9
Special Symbols -, +, *, /, etc.
Whitespaces - Blank Space, tab, carriage return, newline, formfeed
- Other Characters - Python can process all ASCII and Unicode 
characters as part of data or literals"""


""""Variables: A variable is a name given to a memory location in a program.
Variable name should be meaningful and short."""
name = "Zahid" # string
age = 44
print("My name is:", name, "and my age is: ", age)

print(type(name))
print(type(age))

"""Data Types
-Integers (int) --- > 0, 1, 2, 3, -1, -4
-String         .... > "Zahid", 'Hello'
-Float ..... > True, False
-Boolean
-None .... > shows 'no value is stored'
"""

age = 43
a = False
b = None
print(type(age))
print(type(a))
print(type(b))

# Sum, subraction, division, operators
a1 = 4
b1 = 7
sum = a1 + b1
print(sum)

a1 = 4
b1 = 7
difference = a1 - b1
print(difference)

a1 = 9
b1 = 2
division = a1/b1
print(division)
print(a1%b1)
print(a1 == b1)
print(a1!=b1)
print(a1 >= b1)
print(a1>b1)
a1 += 1
print(a1)
a1 -= 3
print(a1)
a1 /= 2
print(a1)

# Comment in Python- Single line code is commented using '#'
# whereas multiline comment can be done with triple commas....""""""

# Type conversion
a = int("4")
b = int(5.5)
print(a+b)


# Logical Operators
print(not True)
print(not False)
print(not a > b)
print(not a>= b)
print(a != b)

val1 = False
val2 = True
print("AND operator:", val1 and val2)
print("OR operator:", val1 or val2)
print("OR operator:", (a == b) or (a < b))



