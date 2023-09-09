s1 = 'Python'
s2 = 'Programming'
s3 = 'I like'

print("{} {} {}".format(s3, s1 ,s2))
print("{0} {2} {1}".format(s3, s1 ,s2))



s1 = 'Python'
s2 = 'Programming'
s3 = '3.7'
print()
print("{t0} {t1} {t2}".format(t0=s2, t1=s1 ,t2=s3))
print("{t1} {t2} {t0}".format(t0=s2, t1=s1 ,t2=s3))
print("{t1} V.{t2} {t0}".format(t0=s2, t1=s1 ,t2=s3))
print(f"{s1} {s2}")