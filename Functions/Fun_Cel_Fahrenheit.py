### Create a function that converts temperature from Celsius to Fahrenheit.
a = 30
def Celsius_Fahrenheit(celsius):
    fahrenheit = (a * 9 /5) + 32
    return fahrenheit

test_temperatures = [0, 30, 22, 60]

for temp in test_temperatures:
    fahrenheit = Celsius_Fahrenheit(temp)
    print(f"{temp} is equal to {fahrenheit: .1} F")