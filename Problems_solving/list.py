##Create a list of favorite fruits: Write a program that asks the user to enter their 5 favorite fruits and stores them in a list. Then print the list.

fav_fruits = []

for i in range(5):
    fruit = input(f"Enter your favorite fruit #{i+1}: ")
    fav_fruits.append(fruit)

print("\nYour favorite fruits are:")
print(fav_fruits)




### Find the sum and average of numbers in a list: Create a list of 10 numbers. Write a program to calculate and print the sum and average of these numbers.

list = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]



numbers_list = sum(list)

avg_num = numbers_list / len(list)

print(numbers_list)
print(avg_num)