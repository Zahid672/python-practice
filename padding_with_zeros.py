# Ask the user for a number. Print this number padded with leading zeros to a width of 5.
user_input = input('Enter a number: ')
# Convert the input to an integer and format it with leading zeros  
formatted_number = f"{int(user_input):05}"
print(formatted_number)

