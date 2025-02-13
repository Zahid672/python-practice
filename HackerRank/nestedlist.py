""""
1. Given the names and grades for each student in a class of N students, store 
them in a nested list and print the name(s) of any student(s) having the second lowest grade.
2. If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
"""

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    students.sort(key=lambda x: x[1])
    second_lowest = sorted(set([x[1] for x in students]))[1]
    for name, score in students:
        if score == second_lowest:
            print(name)