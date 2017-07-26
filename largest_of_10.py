'''str="hello world"
str1=str.split()
print(str1)
a=input()
print(a)
#print(a.split())
print(a[0])
x=a.split()
#print(int((x[0])/2))
x=[int(i) for i in x]
print(type(x))
print(int((x[0])/2))

a=input()
print("given input is",a)
x=a.split()

x=[for i in x:
    int(i)
print("type is",x[0]/2)'''

print("Please provide the required 10 numbers to be sorted..!")
a=input()
x=a.split()
print("length is",len(x))
print(x)
x=[int (i) for i in x]
print("length is",len(x))
print(type(x[0]))

max=x[0]
length=len(x)
for i in range(0,length):
    print("value is",x[i],"\t","max is",max,"\n")
    if(x[i]>max):
        max=x[i]

print("The maximum value is",max)