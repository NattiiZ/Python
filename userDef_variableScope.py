def show_local():
    global x
    y = 10
    x = x+10
    print('x =', x)
    print('y =', y)


x = 5
show_local()
