def apply_operation(func, x, y):
    return func(x, y)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

result = apply_operation(add, 5, 3)
print("Addition Result:", result)

