fullName = input('Enter full name : ')


# Case 1 -----
# name,cut = fullName.split()

# Case 2 -----
# cut = fullName.find(' ')
# name = fullName[:cut]


# Case 3 -----
names = fullName.split()
name = names[0]


print()
print("Your name =", name)
print("Lower name =", name.lower())
print("Upper name =", name.upper())
print("Cappitalize name =", name.capitalize())