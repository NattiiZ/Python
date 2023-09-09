import random

a = random.randint(1, 6)
print('a = ', a)

b = random.random()
print('b = ', b)

c = random.uniform(1.5, 6.5)
print('c = ', c)

d =  random.choice('AEIOU')
# d =  random.choice('['m',2,3,4,'tu',]')
# d =  random.choice('[1,2,3,4,5]')
print('d = ', d)

e = random.randrange(10, 101, 10)
print('e = ', e)