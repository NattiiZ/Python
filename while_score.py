total = 0.0
score = ""
count = 1
while score != "-1":
    score = input(f"Enter score value #{count} : ")
    if score != "-1":
        count += 1
        total += float(score)

count -= 1

print()
print("Number of score :", count)
print("Total score value :", total)
print("Average score : %.2f" % (total/count))