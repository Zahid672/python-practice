l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

# l3 = []

# for i in range(1, len(l1), 2):
#     l3.append(l1[i])
#     print(l3)

# for i in range(0, len(l2), 2):
#     l3.append(l2[i])
#     print(l3)

l3 = l1[1::2] + l2[0::2]
print(l3)