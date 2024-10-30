#### Print a multiplication table: Write a program that takes a number as input and prints its multiplication table (from 1 to 10) using a for loop.

input_number = int(input("Enter the number"))

for i in range(1, 11):
    result = input_number * i

    print(f"{input_number} x {i} = {result}")
