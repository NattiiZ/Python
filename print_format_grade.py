grade1 = int(input('Enter grade 1 (0-4) : '))
grade2 = int(input('Enter grade 2 (0-4) : '))
grade3 = int(input('Enter grade 3 (0-4) : '))
grade4 = int(input('Enter grade 4 (0-4) : '))


total = grade1 + grade2 + grade3 + grade4
credit = 4
GPA = total / credit


print()
print("You have %d subject" %credit)
print("You have total point = %.2f, %d credit" %(total, credit))
print("You get GPA =%5.2f" %GPA)