loop = True
line1 = ('=')*21
line2 = ('-')*21
line3 = ('-')*35
totalPay = 0.0
listItem = ''
order = 0


while loop:
    print(line1)
    print('|'+'Drinks Menu'.center((len(line1))-2)+'|')
    print(line1)
    print('| ' + '0. Quit'.ljust(18) + '|')
    print('| ' + '1. Hot Coffee'.ljust(18) + '|')
    print('| ' + '2. Ice Coffee'.ljust(18) + '|')
    print('| ' + '3. Frappe Coffee'.ljust(18) + '|')
    print('| ' + '4. Calculate Cost'.ljust(18) + '|')
    print(line2)
    
    choice = input('Select Item : ')

    if choice == '0':
        print('Exit Program ...')
        loop = False
    elif choice == '1':
        Item = 'Hot Coffee'
        Qty = input(f'{Item}, how many glasses : ')
        if Qty == '':
            print('Amount is empty.')
            break
        price = 35.0
        total = '%.2f' %(int(Qty)*price)
        totalPay += float(total)
        listItem += (f'{Qty}'.rjust(2) + '   ' + f'{Item}'.ljust(16) + '%.2f'%price + total.rjust(9)) + '\n'
    elif choice == '2':
        Item = 'Ice Coffee'
        Qty = input(f'{Item}, how many glasses : ')
        if Qty == '':
            print('Amount is empty.')
            break
        price = 50.0
        total = '%.2f' %(int(Qty)*price)
        totalPay += float(total)
        listItem += (f'{Qty}'.rjust(2) + '   ' + f'{Item}'.ljust(16) + '%.2f'%price + total.rjust(9)) + '\n'
    elif choice == '3':
        Item = 'Frappe Coffee'
        Qty = input(f'{Item}, how many glasses : ')
        if Qty == '':
            print('Amount is empty.')
            break
        price = 60.0
        total = '%.2f' %(int(Qty)*price)
        totalPay += float(total)
        listItem += (f'{Qty}'.rjust(2) + '   ' + f'{Item}'.ljust(16) + '%.2f'%price + total.rjust(9)) + '\n'
    elif choice == '4':
        if listItem != '':
            order += 1
            print(f'\nOrder #{order}:')
            print(line3)
            print('Qty'.ljust(5) + 'Item'.ljust(16) + 'Price' + 'Total'.rjust(9))
            print(line3)
            print(listItem)
            print(line3)
            print('Total : %.2f Bath' % totalPay)
            listItem = ''
            totalPay = 0
        else:
            print('Oder is empty.')

        print()
    else:
        print('Item invalid, Please select again.')
        
    print()