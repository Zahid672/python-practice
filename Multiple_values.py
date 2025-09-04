def calculation(a, b):
    sum = a + b
    subtract = a - b

    return sum, subtract  # Returning multiple values as a tuple

result = calculation(40, 20)
print(result)  # This will print the tuple (60, 20)