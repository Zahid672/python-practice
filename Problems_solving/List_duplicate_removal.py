### Remove duplicates: Write a program to remove all duplicate elements from a list.

original_list = [2, 3, 3, 2, 4, 5, 4, 7]

new_list = []

for items in original_list:
    if items not in new_list:
        new_list.append(items)
        
print(new_list)