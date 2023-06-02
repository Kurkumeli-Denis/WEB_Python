A = [[3, 6, 1], [2, 7, 6], [8, 6, 3], [5, 1, 5]]
transResult = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
for a in range(len(A)):
    for b in range(len(A[0])):
        transResult[b][a] = A[a][b]
for res in transResult:
    print(res)
