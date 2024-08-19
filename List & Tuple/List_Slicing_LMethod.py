# List slicing is Similar to string slicing
lst_name = [0, 2, 3, 4, 9, 22]
print(lst_name[:]) #output: [0, 2, 3, 4, 9, 22]
print(lst_name[2:]) #output: [3, 4, 9, 22]
print(lst_name[-4:-1]) # [3, 4, 9]

#List Methods
list = [55, 21, 3]
list.append(44) #add one element at the end
print(list) # output: [55, 21, 3, 44]
print(list.sort()) #sorts in ascending order
print(list) #output: [3, 21, 44, 55]
print(list.sort(reverse=True)) #sorts in descending order
print(list) #output: [55, 44, 21, 3]
print(list.reverse()) #reverses list
print(list) #output: [3, 21, 44, 55]
list.remove(21) # remove first occurence of element
print(list) #output: [3, 44, 55]
print(list.insert(2,88)) #insert element at index
print(list) # output: [3, 44, 88, 55]
print(list.pop(0)) #removes element idx
print(list) #output: [44, 88, 55]

#using list. we can see all the list Methods.


