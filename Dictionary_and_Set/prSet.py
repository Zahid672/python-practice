###write a program to enter marks of 3 subjects from the user and store them in a dictionary.
# Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

marks = {}

user_input1 = int(input("Enter marks for first subject: "))
marks.update({"maths": user_input1})
user_input2 = int(input("Enter marks for second subject: "))
marks.update({"pashto": user_input2})
user_input3 = int(input("Enter marks for subject third: "))
marks.update({"Hindi": user_input3})

print(marks)