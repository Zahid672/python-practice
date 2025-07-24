# Write a Python code to print the following number pattern using a loop.
n = 20
for i in range(1, n + 1, 5):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()