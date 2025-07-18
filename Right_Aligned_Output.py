#Ask the user for a word and a number. Print the word right-aligned in a field of width 20, followed by the number.
user_input1 = input('Enter a word: ')
user_input2 = input('Enter a number: ')
print(f'{user_input1:>20}{user_input2}')