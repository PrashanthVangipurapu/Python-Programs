a=int(input())
b=int(input())
print("palindrome in the range of",a,"and",b)

for x in range(a,b):
    sum=0;
    p=x
    while(p>0):
         n = int(p % 10)
         p = int(p / 10)
         sum=sum*10+n;
    if(sum==x):
        print(x," is palindrome ")



