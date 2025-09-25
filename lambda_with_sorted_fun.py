# Use a lambda with the sorted() function to sort a list of tuples based on the second element
data = [(1, 'banana'), (2, 'apple'), (3, 'cherry')]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)