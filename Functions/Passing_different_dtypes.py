

## example 1.

def diff_dtype_function(food):
    """You can send any data types of argument to a function 
    (string, number, list, dictionary etc.), and it will be treated 
     as the same data type inside the function. E.g. if you send a List as an argument, 
     it will still be a List when it reaches the function:"""
    for x in food:
        print(x)
        
fruits = ["mango", "banana", "cherry"] 
"""fruits is list datatype"""
people = ("zahid", "saeed")
"""people is tuple datatype"""
countries_capitalcity = {"Afg" : "Kabul",
                         "Iran": "Tehran"}
"""the datatype of countries_capitalcity is dictionary"""

diff_dtype_function(people)

diff_dtype_function(fruits)
diff_dtype_function(countries_capitalcity)