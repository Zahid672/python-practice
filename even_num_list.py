def even_num_list(num_list):
    for num in range(4, 30):
        if num % 2 == 0:
            num_list.append(num)
    return num_list
result = even_num_list([])
print(result)  # Output: [4, 6, 8, 10,