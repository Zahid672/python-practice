first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

result_set = first_set.intersection(second_set)
print(result_set)

# print the fist set without the common elements using remove method
for element in result_set:
    first_set.remove(element)

print(first_set)