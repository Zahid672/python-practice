##Remove first n characters from a string
s = "PYnative"
s1 = s.replace("PYnat", "")
print(s1)

### using for loop
s = "PYnative"
s1 = ""
for i in s:
    if i not in "PYnat":
        s1 = s1 + i
print(s1)


### using list comprehension
s = "PYnative"
s1 = "".join([i for i in s if i not in "PYnat"])
print(s1)