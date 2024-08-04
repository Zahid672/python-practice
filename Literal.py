# Literal is a raw data given to a variable. In Python, there are various types of literals.

a = 0b1010 #Binary Literals
b = 100 #Decimal literals
c = 0o310 #Octal Literals
d = 0x12c #Hexadecimal Literals

#Float Literals
float_1 = 10.5
float_2 = 1.5e2
float_3 = 1.5e-3

#Complex Literals
x = 3.14j

print(a,b,c,d)
print(float_1, float_2, float_3)
print(x, x.imag, x.real)

# String Literals
string = ' This is Python'
strings = "This is Python"
Char = "C"
multiline_str = """"This is a multiline string with more than one line code."""



print(string)
print(strings)
print(Char)
print(multiline_str)

#Boolean Literal
a = True + 5
b = False + 9

print("a:", a)
print("b:", b)

# Special Literals
a = None
print(a)
