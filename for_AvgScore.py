total = 0.0
Max = 6

for n in range(1, Max):
    score = float(input(f'Enter score {n} : '))
    total = total + score

print()
print('total score value =', total)
print('Average score =', total/5)