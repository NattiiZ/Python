def main():
    message = input('Enter string : ')
    print_string(message)


def print_string(text):
    if len(text) > 0:
        print(text)
        print_string(text[:len(text)-1])
    

main()