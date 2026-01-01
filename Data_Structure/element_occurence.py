sample_list = [34, 54, 67, 89, 11, 43, 94, 1, 24, 66, 78, 99, 100, 234]

empty_dict = {}
for element in sample_list:
    empty_dict[element] = empty_dict.get(element, 0) + 1

print(empty_dict)