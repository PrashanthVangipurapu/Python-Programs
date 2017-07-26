a=int(input())
b=int(input())
c=int(input())

if a**2+b**2==c**2:
    print('The given sides belong to a right angled triangle')
    print('The area of the triangle is', str(int(1/2*a*b)))
else:
    print('the given sides do not belong to the right angled triangle')
    s=a+b+c/2;
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    print('the area is',str(int(area)))
print (math.sin(30))

