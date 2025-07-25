total_sum = 0
user_input = input("Enter a number: ")
for i in range(1, int(user_input) + 1):
    total_sum += i
    print("The sum of all numbers is:", total_sum)
    print("The average of all numbers is:", total_sum / int(user_input))