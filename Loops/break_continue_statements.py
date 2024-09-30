## Break: used to terminate the loop when encounter (come across)
## Continue: terminate execuation in the current iteration & continues execution of the loop with the next iteration. Continue act as skip

i = 1

while i <= 5:
    print(i)
    if(i == 4):
        break
    i += 1
print('end of loop')


nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)

x = 36

while i < len(nums):
    if(nums[i] == x):
        print("Found at idx", i)
        break
    else:
        print("finding..")
    i += 1

print('end of loop')



i = 0
while i <= 5:
    if(i == 3):
        i += 1
        continue
    print(i)
    i += 1


    
