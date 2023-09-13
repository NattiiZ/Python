def main():
    print()
    print_Triangle()
    print()
    print_Triangle(3)
    print()
    print_Triangle(8)


def print_Triangle(num=5):
    for n in range(1, num+1):
        text = '#'*n
        print(text)


main()