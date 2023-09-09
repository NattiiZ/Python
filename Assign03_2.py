print ('========== Painting Calculator ==========\n')
width = float(input('Enter the width of the house (m) : '))
length = float(input('Enter the length of the house (m) : '))
height = float(input('Enter the height of the house (m) : ' ))


scale = (width * length * height)
liter = (scale / 2.5)
bucket = int(liter / 4)
cost = (bucket * 200)


print()
print('Total painting area =', scale, 'Square Meter.')
print('Total amount of color =', liter, 'Liter.')
print('All used paint bucket =',  bucket, 'bucket.')
print('Total purchase amount =', cost,'$')
