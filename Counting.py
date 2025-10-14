#Count all letters, digits, and special symbols from a given string

str1 = "P@#yn26at^&i5ve"
count = 0
for i in str1:
    count += 1
print("Total characters:", count)
print("Total characters:", len(str1))
print("Total letters:", sum(c.isalpha() for c in str1))
print("Total digits:", sum(c.isdigit() for c in str1))
print("Total special characters:", sum(not c.isalnum() for c in str1))

