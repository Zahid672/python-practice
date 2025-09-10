def different_name_function(name, age):

    print(f"{name} is {age} years old.")

different_name_function("Alice", 30)

new_name_function = different_name_function
new_name_function("Bob", 25)  # Output: Bob is 25 years old.
print(new_name_function)  # Output: <function different_name_function at ...>  





    
    