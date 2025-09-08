def outer_function(a, b):
    def inner_function(sum_ab):
        return sum_ab + 5
    return inner_function(a + b)

result = outer_function(3, 4)
print(result)  # Output: 12