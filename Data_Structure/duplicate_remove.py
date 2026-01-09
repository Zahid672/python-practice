sample_list = [87, 45, 41, 65, 94, 99, 94]
unique_list = []
for item in sample_list:
    if item not in unique_list:
        unique_list.append(item)
print("List after removing duplicates:", unique_list)

Tuple = (23, 45, 67, 89, 45, 23, 67)
print('min:', min(Tuple))
print('max:', max(Tuple))
