s1 = "Abc"
s2 = "Xyz"

for i in range(min(len(s1), len(s2))):
    print(s1[i] + s2[-(i + 1)], end="")