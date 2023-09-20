A = [[[1, 2], [3,4]],[[5, 6], [7, 8]]]

for r in range(len(A)):
    for c in range(len(A[0])):
        for d in range(len(A[0][0])):
            print(A[r][c][d])
            
            
print()
# ----------------------------------------

B = []
n = 1

for r in range(2):
    B.append([])
    for c in range(2):
        B[r].append([])
        for d in range(2):
            B[r][c].append(n)
            n += 1
print(B)