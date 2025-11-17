str1 = "PYnative29@#8496"
sum_digits = 0
count_digits = 0

for char in str1:
    if char.isdigit():
        sum_digits += int(char)
        count_digits += 1

if count_digits > 0:
    avg_digits = sum_digits / count_digits
    print("The average of the digits is:", avg_digits)
else:
    print("No digits found.")

