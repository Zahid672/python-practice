my_list = [10,20, 30, 40, 50, 60, 70, 80, 90, 100]
odd_list = []
for i in range(len(my_list)):
    if i % 2!= 0:
        odd_list.append(my_list[i])
print(odd_list)