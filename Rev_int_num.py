# num = 24567
# print(str(num)[-1:-6:-1])

rev_num = 0
num = 24567
while num > 0:
    rev_num = rev_num * 10 + num % 10
    num //= 10
print(rev_num)
