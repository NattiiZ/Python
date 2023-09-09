amount = int(input("Enter amount product : "))
price = int(input("Price per unit : "))

total =  price * amount
print("Total money = ", total)

pay = float(input("Enter pay money : "))
change = pay - total
print("Money change = " , change)
