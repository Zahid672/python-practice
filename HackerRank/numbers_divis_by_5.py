##Display numbers divisible by 5
Given_list = [10, 5, 33, 44, 65]
print("The available list is:", Given_list)
print("Divisible by 5:")
for items in Given_list:
    if items % 5 == 0:
        print(items)