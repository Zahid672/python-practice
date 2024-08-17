# nesting matlab pa yaw statement ki danana bal statement likal.
age = 100

if(age >= 18):
    if(age >= 99):
        print("cannot drive")
    print("can drive")

else:
    print("cannot drive")


#write a program if a number entered by the user is odd or even.
number = int(input("Enter an integer: "))
if(number % 2 == 0):
    print("Even number")

else:
    print("Odd number")

#write a program to find the greates of 3 numbers entered by the user.
a = int(input("Enter a first number: "))
b = int((input("Enter a second number: ")))
c = int(input("Enter a third number: "))
if(a > b and a > c):
    print("first number is greatest", a)
elif(b > a and b > c):
    print("second number is the greatest", b)
else: 
    print("third number is the greatest", c)


num = int(input("Enter any number: "))
if(num % 7 == 0):
    print(num,'is divisible by 7')
else:
    print(num, "not divisible by 7")
