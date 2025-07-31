list1 = [10, 20, 30, 40, 50]
# print(list1[::-1])    # Output: [50, 40, 30, 20, 10]
for i in range(len(list1)-1, -1, -1):
    print(list1[i], end=' ')