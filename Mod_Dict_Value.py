### Access and modify dictionary values: Create a dictionary representing a person with keys for "name", "age", and "city". Print the person's age, then update their age to a new value and print the updated dictionary.

dict = {"Name": "Khan",
        "age": "35",
        "City": "Peshawar"}

print(dict["age"])

dict.update({"age":"99"})
print(dict["age"])