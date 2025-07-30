row_value = 5
inner_value = 5
for i in range(0, row_value + 1):
    for j in range(inner_value-i,0, -1):
        print(j, end=' ')
    print()