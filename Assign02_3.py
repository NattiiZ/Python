amount = int(input('Enter investment amount : '))
rate = float(input('Enter interest rate : '))/100
year = int(input('Enter the number of years : '))

fv = amount*(1+rate)**year

print()
print('Future value =', fv)