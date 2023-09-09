import math

numberF = float(input("Enter flaot number : "))
numberI = int(input("Enter integer number : "))

print()
print(math.ceil(numberF))
print(math.floor(numberF))
print(abs(-numberI))
print(math.factorial(numberI))
print(math.pow(numberI, 2))
print(math.sqrt(numberI))
print(math.trunc(numberF))
print()

angle = float(input('Enter angle : '))
radian = math.radians(angle)

print(math.sin(radian))
print(math.cos(radian))
print(math.tan(radian))
print(math.degrees(radian))
print(math.radians(angle))
print(math.gcd(7, 17))
print(math.pi)