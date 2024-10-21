##Create a list of favorite fruits: Write a program that asks the user to enter their 5 favorite fruits and stores them in a list. Then print the list.

fav_fruits = []

for i in range(5):
    fruit = input(f"Enter your favorite fruit #{i+1}: ")
    fav_fruits.append(fruit)

print("\nYour favorite fruits are:")
print(fav_fruits)


