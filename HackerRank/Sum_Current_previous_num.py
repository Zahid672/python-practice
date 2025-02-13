## Write a Python code to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number
previous_num = 0
for i in range(10):
    sum = i + previous_num
    print("Current Number", i, "Previous Number", previous_num, sum)
    previous_num = i