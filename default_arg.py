def show_empoyee(name, salary = 9000):
    print("Name:", name, "Salary:", salary)
    return show_empoyee

emp_1 = show_empoyee("Khan", 8000)
emp_2 = show_empoyee("John")  # salary will use the default value
print(emp_1)  # This will print the function itself
print(emp_2)  # This will also print the function itself

