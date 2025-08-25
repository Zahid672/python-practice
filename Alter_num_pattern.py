def alter_num_pattern(n):
    num = 1
    for i in range(1, n + 1):
        if i % 2 != 0:
            for x in range(num, num + i):
                print(x, end=" ")
            print()
        else:
            for y in range(num + i - 1, num - 1, -1):
                print(y, end=" ")
            print()
        num += i

alter_num_pattern(5)
