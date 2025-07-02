A = [1, 2, 10], [4, 3, 9]
B = [0, 7, 8], [11, 1, 12]
result = [[0, 0, 0], [0, 0, 0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] + B[i][j]
        
for res in result:
    print(res)