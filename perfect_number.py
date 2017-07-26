'''PERFECT-NUMBER'''
sum=0
a=int(input())
for x in range(1,(int(a/2)+1)):
    if ((a%x)==0):
        sum+=x

if(sum==a):
    print(a,"is a perfect number")
else:
    print(a,"is not a perfect number")

'''a=int(input())
print(a)

x=a%2
print(x)'''


