# Write a Python code to print the following number pattern using a loop.
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()