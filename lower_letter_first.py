## Arrange string characters such that lowercase letters should come first
def arrange_string(s):
    lower_case = ''.join([char for char in s if char.islower()])
    upper_case = ''.join([char for char in s if char.isupper()])
    return lower_case + upper_case

input_str = "PyNaTive"
output_str = arrange_string(input_str)
print(output_str)  # Output: "yivePNTa"



