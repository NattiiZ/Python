from random import randint


student = int(input('Enter number of student : '))
subject = int(input('Enter number of subject : '))
    
scores = []
for r in range(student):
    scores.append([])
    for c in range(subject):
        scores[r].append(randint(0, 100))
            
for score in (scores):
    print(score)
    print()

