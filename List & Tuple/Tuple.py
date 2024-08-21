"""Tuples in python is a builtin datatype that lets
 us create immutable sequences of values. For example 
 the value of list datatype can be changed (mutable), however, 
 the value of tuple datatype cannot be changed (immutable).
   we use paranthesis in creating Tuple """

Tup = (9 , 0, 4, 3, 2)
print(Tup)

print(Tup[0])
print(Tup[1])

#Tup[0] = 7 will give us error

print(Tup[0:])
print(Tup[2:4])

Tupl = (2,)
print(Tupl)

# Tuple Methods
# Tpl1 = (5, 6, 3, 2, 2)
print(Tup.index(2))

print(Tup.count(2))

# Write a program to ask the user to enter names of their 3 favorite movies & store them in a list.
movies_name1 = input("Enter your first favorite movie name ")
movies_name2 = input("Enter your second favorite movie name ")
movies_name3 = input("Enter your third favorite movie name ")
print("my favorite movie name is: ", movies_name1)
print("my favorite movie name is: ", movies_name2)
print("my favorite movie name is: ", movies_name3)
concat = [movies_name1,movies_name2,movies_name3]
print(concat)

# Write a program to ask the user to enter names of their 3 favorite movies & store them in a list.
movies = []
mov1 = input("Enter your first favorite movie name ")
mov2 = input("Enter your second favorite movie name ")
mov3 = input("Enter your third favorite movie name ")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)

# Write a program to ask the user to enter names of their 3 favorite movies & store them in a list.
movies = []
movies.append(input("Enter your first favorite movie: "))
movies.append(input("Enter your second favorite movie:"))
movies.append(input("Enter your third favorite movie: "))

print(movies)

# write a program to count the number of students with the "A" grade in the following tuple.
lis = ["C", "D", "A", "B", "A", "A", "B"]
print(lis.count("A"))

# Store the above values in a list & sort them from A to D
lis = ["C", "D", "A", "B", "A", "A", "B"]
print(lis.sort())
print(lis)