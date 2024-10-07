### Write a function that takes a person's name as input and prints a greeting message
def greet(name):
    name = input("Enter your name: ")
    print("Greeting", name)

greet(2)

### Create a function that calculates and returns the area of a rectangle given its length and width.
def AOR(length, width):
    area = length * width
    print(area)

AOR(3,4)


### Write a function that takes a list of numbers and returns the sum of all even numbers in the list.
def sum_even_numbers(numbers):
    """
    This function takes a list of numbers and returns the sum of all even numbers in the list.
    
    :param numbers: A list of numbers
    :return: The sum of all even numbers in the list
    """
    even_sum = 0
    for num in numbers:
        if num % 2 == 0:  # Check if the number is even
            even_sum += num
    return even_sum

# Test the function
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_even_numbers(test_list)
print(f"The sum of even numbers is: {result}")


### Define a function that checks if a given number is prime and returns True or False.

def is_prime(number):
    """
    This function checks if a given number is prime.
    
    :param number: The number to check for primality
    :return: True if the number is prime, False otherwise
    """
    # Numbers less than 2 are not prime
    if number < 2:
        return False
    
    # Check for divisibility from 2 to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    
    # If no divisors are found, the number is prime
    return True

# Test the function
test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 97, 100]
for num in test_numbers:
    result = is_prime(num)
    print(f"{num} is prime: {result}")

        
    
        
