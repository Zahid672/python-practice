##Write a Python code to remove characters from a string from 0 to n and return a new string.

def remove_char(word, n):
    print('original word:', word)
    x = word[n:]
    return x
    
    
print('Removing characters from a string')
print(remove_char('PYnative', 4))
print(remove_char('PYnative', 2))