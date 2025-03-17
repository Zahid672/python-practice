userinput = input("Enter string: ")
# print("Original string:", userinput)
# str_len = len(userinput)

# for i in range(0, str_len - 1, 2):
#     print([i], userinput[i])
    
    
    
x = list(userinput)
for i in x[0::2]:
    print(i, end = "")