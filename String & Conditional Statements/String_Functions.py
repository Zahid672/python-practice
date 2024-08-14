str1 = "i work in South Korea"
print(str1.endswith("ea"))   #returns true if string ends with substr
print(str1.endswith("a"))
print(str1.endswith("a."))

print(str1.capitalize()) # capitalize 1st character


print(str1.replace("i", "We")) #Replaces all occurrences of old with new
print(str1.replace("South", "North"))

print(str1.find("work")) # returns 1st index of 1st occurrence
print(str1.find("Korea"))
print(str1.find("zahid"))

print(str1.count("in")) #counts the occurrence of substring in string (substring means small string.)
print(str1.count("o"))
print(str1.count("i"))


# write a program to input user's first name & print its length.
First_name = input("Enter your first name: ")
Length = ("length of your name is:", len(First_name))
print(Length)

#write a program to find the occurrence of "$" in a string
str2 = "$Hello, how are you$?"
print(str2.count("$"))

