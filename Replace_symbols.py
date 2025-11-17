str1 = '/Jon is @developer & musician!!'
symbols = ['@', '&', '!', '/']

for symbol in symbols:
    str1 = str1.replace(symbol, '#')
print(str1)
