A = [[1, 2, 3], [4, 5, 6]]

print(len(A))
print(len(A[0]))
print(A[0][0])

print()

for row in range(len(A)):
    for col in range(len(A[0])):
        print(A[row][col])
        
        
print("\n\n")

B = []
for row in range(3):
    B.append([])
    for col in range(4):
        B[row].append(col)
        
        
print(B)