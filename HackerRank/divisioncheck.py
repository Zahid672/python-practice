###Display numbers divisible by 5

numbers = [10, 20, 33, 46, 55]
for n in numbers:
    if(n% 5 == 0):
        print(f"{n} is divisible by 5")
    else:
        print(f"{n} is not divisible by 5")
    