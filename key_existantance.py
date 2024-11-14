##Check if a key exists: Write a function that takes a dictionary and a key as input. The function should return True if the key exists in the dictionary, and False otherwise.
def key_exists(dictionary, key):
    return key in dictionary

fruits = {
    "apple": "red",
    "banana": "yellow",
    "grape": "green"
}
print(key_exists(fruits, "apple"))
print(key_exists(fruits, "orange"))