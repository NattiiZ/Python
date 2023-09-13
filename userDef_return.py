import math

def main():
    loop = True

    while (loop):
        print('='*24)
        print(' Program calculate area')
        print('='*24)
        menu = selectMenu()
        if menu == 1:
            radius = int(input('Enter radius : '))
            print('Area of Circle =', Cal_Circle(radius))
        elif menu == 2:
            width = int(input('Enter width : '))
            height = int(input('Enter height : '))
            print('Area of Rectangle =', Cal_Rectangle(width, height))
        elif menu == 3:
            base = int(input('Enter base : '))
            height = int(input('Enter height : '))
            print('Area of Triangle =', Cal_Triangle(base, height))
        elif menu == 4:
            print('Exit...')
            loop = False
        else:
            print('Invalid menu.')
        print()


def selectMenu():
    # print('Menu')
    print('1. Circle\n2. Rectangle\n3. Triangle\n4. Exit')
    menu = int(input('Please choose : '))
    print('='*24)

    return(menu)

def Cal_Circle(radius):
    area = round(math.pi*math.pow(radius, 2), 2)
    return(area)

def Cal_Rectangle(width, height):
    area = width*height
    return(area)

def Cal_Triangle(base, height):
    area = (base*height)/2
    return(area)


main()