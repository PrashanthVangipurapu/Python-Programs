x=10
y=20
print ("before swap")
print ("x is",x)
print("y is",y)
x=x+y
y=x-y
x=x-y
print("\nafter swap")
print("x is",x)
print("y is",y)


print("****************")
x=10
y=20

for a in range(1,10):
    print(x)
    print(y)
    y=x+y
    x=y-x
    print()
else:
    print("for loop completed..!!")
