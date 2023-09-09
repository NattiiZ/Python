#keyword test------------------------

import keyword

print(keyword.kwlist)

print(keyword.iskeyword('if'))

print(keyword.iskeyword('Test'))



print("\n\n\n\n")




#check type------------------------

Name = 'Nat'
print(Name)
type(Name)


A = 18
B = 3.73
C = 'N'
D = True

#print(A,B,C,D)
type(A)
type(B)
type(C)
type(D)

type(40)
type(1.7)
type('name')
type(False)



print("\n\n\n\n")




#comment------------------------

#this is comment

'''10101000101010101010010
10101000101010101010010
100101000010111001100101000010111001'''



print("\n\n\n\n")




#multi print------------------------

A = 12
B = 7.1

print(A,B)

A = B = C = 11
print(A,B,C)


a,b,c = 1,2,3
print(a,b,c)


print('test', 'hello',sep='|')
print('test', 'hello',sep='')
print('test',end='')



print("\n\n\n\n")




#print------------------------

print("\n\n\n\n")

ver = 3.11

print ('Python',ver,end='')
print('.4')

print ('Python',ver)
print('.4')

name = "nat"
text = "this Proj create by " + name + "."
print(text)


Strg = "Python " + str(ver)
print(Strg)



print("\n\n\n\n")




#operator------------------------

print("HelloWorld!\nHelloWorld!\nHelloWorld!")
print("Tab1\tTab1\tTab1\tTab1")

print("C:\\User\\")
print("Name : \"Nat\"")
print("my name\'s Nat")



print("\n\n\n\n")




#input------------------------

'''input("Enter ")'''
Name = input("Enter Name : ")
print(Name)


##Size Calculate##
'''height = float(input("Enter Height : "))
weight = float(input("Enter Weight : "))'''

height,weight = float(input("Enter Height : ")),float(input("Enter Weight : "))

size = height*weight
print(size)



print("\n\n\n\n")


