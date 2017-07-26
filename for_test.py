'''c=int(input())
for x in range(2,c):
    print(x)'''

a=input()
a=a.split()
x=[int (i) for i in a]
for i in range(1,len(a)):
    print(i)
a=10
print(type(a))

b=20.5
print(type(b))
c=20.541000
print(type(c))