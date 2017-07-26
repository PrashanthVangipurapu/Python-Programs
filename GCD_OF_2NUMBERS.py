print("Enter the two numbers..!!")
a=int(input())
b=int(input())
print("the entered numbers are",a,b)
if(a<b):
    min=a;
else:
    min=b;
gcd=0
for i in range(1,min+1):
    if(a%i==0):
        if(b%i==0):
            gcd=i

print("gcd of ",a,"and",b,"is",gcd)

