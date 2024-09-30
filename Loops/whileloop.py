### The loops condition depends on variable (variable matlab jis ka value change ho sakta ho)
i = 1

while i <= 100: ## called stopping condition
    print(i)
    i += 1


numbers = 100
# ###
while numbers >= 1: ### called stopping condition
    print(numbers)
    numbers -= 1


### print the multiplication table of a number n.
i = 1

while i <= 10: ### The loops condition depends on variable (variable matlab jis ka value change ho sakta ho)
    print(3*i)
    i +=1

i = 1 

while i <= 10: ## index hi hamara wo variable ha jis k basis pe hamara loop run karay ga
    print(i*i)
    i += 1


nums = [1, 4, 9, 16, 25, 36, 49, 64]

idx = 0

while idx < len(nums):
    print(nums[idx])
    idx += 1


cricketers = ["Ponting", "Mcgrath", "Gilchrist", "Steve"] # traverse

index = 0

while index < len(cricketers):
    print(cricketers[index])
    index += 1


## search for a number x in this tuple using loop:

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 25

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("FOUND at idx", i)
    else:
        print("Finding..")
    i += 1
    
    