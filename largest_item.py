def find_largest_item(items):
    x = [4, 6, 8, 24, 12, 2]
    largest_item = []
    for item in x:
        if item == max(x):
            largest_item.append(item)
            return largest_item
        
result = find_largest_item([])
print(result)  # Output: [24]