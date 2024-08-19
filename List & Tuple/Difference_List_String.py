#lists are mutable while strings are not mutable. for example:
str = "Hello there"
print(str[0])
# str[0] = "Z"  ---- > not allowed

lst = [99, 88, 77, 45, 66, 33]
lst[3] = 22
print(lst)

lst1 = ["Zahid", 80, 74, "Afg"]
lst1[1] = 90
print(lst1)
