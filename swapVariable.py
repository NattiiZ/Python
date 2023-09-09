#Swap test

A = "a"
B = "b"
print("Before A =",A,"| B =",B)
Z = A
A = B
B = Z
print("After A =",A,"| B",B)

X = 'x'
Y = 'y'

X, Y = Y, X
print("X =", X)
print("Y =", Y)


