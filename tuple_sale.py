def main():
    Sales = ()
    count = 1
    loop = True

    while loop:
        sale = float(input(f'Enter sale {count} (-1 ot Exit) : '))
        if sale > -1.0:
            Sales += (sale, )
            count += 1
        elif sale == -1.0:
            loop = False

    Totals = sum(Sales)
    Rate = checkRate(Totals)
    Commission = Totals * Rate
    print(f'Total sales : {Totals}')
    print(f'Commission Rate : {Rate*100}%')
    print(f'Total commission : {Commission}')
    print()



def checkRate(sale):
    Rates = (0.30, 0.25, 0.20, 0.15, 0.10, 0.05, 0.0)
    TotalSales = (1000000.0, 750000.0, 500000.0, 250000.0, 100000.0, 1.0, 0.0)
    for i in range(len(TotalSales)):
        if sale > TotalSales[i]:
            return(Rates[i])
        else:
            return(0)


main()