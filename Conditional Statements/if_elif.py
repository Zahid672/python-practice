light = "green"

if(light == "red"):
    print("Stop")

elif(light == "green"):
    print("Go")
elif(light == "yellow"):
    print("Look") #indentation in python is very important.

print("end of code")

marks = int(input("Enter student marks :"))
if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"

print("grade of the student: ", grade)
