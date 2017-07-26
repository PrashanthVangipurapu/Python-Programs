#Maximum of 3 numbers
str=input('Ask from user');
print(str);
print('Enter the first number')
a=float(input())
print(a)
print('enter the second number')
b=float(input())
print(b)
print('enter the third number')
c=float(input())
print(c)
#print('All 3 were given')
if a>b:
    if a>c:
        print('a is greater',a)
    else:
         print('c is greater',c)
else:
    if b>c:
        print('b is greater',b);
    else:
        print('c is greater',c);

