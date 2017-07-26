#a=int(input())
#b=int(input())
#print("palindrome in the range of",a,"and",b)
a=int(121)
sum=0;
p=int(a);
print("p is",p)
count=0;
while(p>0):
    n=int(p%10)
    #print("the value of n is",n)
    p=int(p/10)
    #print("the value of p is ",p)
    sum=sum*10+n
    #print("the value of sum is",sum)
    count+=1

print("the value of count is",count)
if (sum==a):
    print("in if block");
    print("121 is a palidnrome")
else:
     print("in else block");
     print("not a palindrome")

'''for x in range(a,b):
    sum=0;
    p=x
    while(p>0):
         n = p % 10
         p = p / 10
         sum=sum*10+n;
    if(sum==x):
        print(x," is palindrome ")
'''


