print("Displaying first 10 fibanocci numbers");
print("Enter the first number--")
a=int(input());
print("Enter the second number--")
b=int(input())


print("number of fibanocci sequences you want")
c=int(input())
print(a)
print(b)
for x in range(2,c):

    d=a+b;
    print(d)
    a=b
    b=d

else:
    print("Fibannocci completed..!!")

