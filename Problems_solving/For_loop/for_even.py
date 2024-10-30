## Print even numbers from a list: Given a list of numbers, use a for loop to print only the even numbers from the list.

List = [3, 2, 1, 5, 6, 8, 9]

for i in List:
    if i % 2 == 0:
        print(f"{i} is even number")
    else: 
        print(f"{i} is odd number")

