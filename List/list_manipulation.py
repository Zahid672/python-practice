my_list = [10, 20, 30, 40, 50]
modified_list = my_list[1] = 200
print('After changing second element:', my_list)

appended_list = my_list.append(600)
print('After appending 600:', my_list)

inserted_list = my_list.insert(2, 300)
print('After inserting 300 at index 2:', my_list)

removed_list = my_list.remove(600)
print('After removing 600:', my_list)

pop_element = my_list.pop(0)
print('After popping element at index 0:', my_list)