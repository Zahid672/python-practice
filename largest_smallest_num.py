num1 = 987654321
num2 = -5082

# absolute values
abs_num1 = abs(num1)
abs_num2 = abs(num2)
print("Absolute value of num1:", abs_num1)
print("Absolute value of num2:", abs_num2)

abs_num1 = str(abs_num1)
abs_num2 = str(abs_num2)

largest_num = []
smallest_num = []

# Finding largest number
for digit in abs_num1:
    largest_num.append(digit)
largest = max(largest_num)
print("Largest digit in num1:", largest)

# Finding smallest number
for digit in abs_num1:
    smallest_num.append(digit)
smallest = min(smallest_num)
print("Smallest digit in num1:", smallest)

largest_num = []
smallest_num = []

# Finding largest number
for digit in abs_num2:
    largest_num.append(digit)
largest = max(largest_num)
print("Largest digit in num2:", largest)

# Finding smallest number
for digit in abs_num2:
    smallest_num.append(digit)
smallest = min(smallest_num)
print("Smallest digit in num2:", smallest)