## Write a program that asks the user to enter a number. If the number is greater than 10, print "The number is greater than 10", otherwise print "The number is 10 or less".
user_input = float(input("Enter a number: "))
if user_input > 10:
    print("The number is greater than 10")
else: 
    print("The number is 10 or less")

### Create a program that asks for the user's age. If the age is 18 or older, print "You are eligible to vote", otherwise print "You are not eligible to vote".

user_age = int(input("Enter your age: "))

if user_age >= 18:
    print("You are eligible to vote")

else:
    print("You are not eligible to vote")


### Write a script that prompts the user to enter a fruit name. 
# If the fruit is "banana", print "Yellow", if it's "apple", print "Red", for any other fruit, print "Unknown".

fruit_name = input("Enter fruit name: ")

if fruit_name == "banana":
    print("Yellow")
elif fruit_name == "apple":
    print("red")
else:
    print("Unknown")

##Make a program that asks for two numbers. If the first number is larger than the second, print "The first number is larger", 
#otherwise print "The second number is larger or they are equal".

First_number = float(input("Enter first number: "))
Second_number = float(input("Enter second number: "))

if First_number > Second_number:
    print("first number is larger")

else:
    print("Second number is larger")


### Create a script that asks the user to enter a letter. If it's a vowel (a, e, i, o, u), print "It's a vowel!", otherwise print "It's a consonant".

