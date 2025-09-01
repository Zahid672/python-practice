def func1(*vars):
    print(*vars, sep="\n")
    return func1

f1 = func1(20, 40, 60)
print(f1)  # This will print None because func1 does not return anything

f2 = func1(80, 100)
print(f2)  # This will also print None because func1 does not return anything