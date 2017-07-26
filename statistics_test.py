import statistics as s
import random as r
x=[]
print("enter low range")
a=int(input())
print("enter high range")
b=int(input())

for i in range(0,10):
    x.append(r.randint(a,b))

print (x)

mean=s.mean(x)
print("mean is",mean)
median=s.median(x)
print("median is",median)
(stdev)=s.stdev(x)
stdev1=round(stdev)
print("std deviation is",stdev)
print("std deviation is",stdev1)