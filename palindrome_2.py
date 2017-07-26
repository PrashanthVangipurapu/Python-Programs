a=input("enter a string")
print("The string is",a)


def reverse(a):
    new_string=' '
    index=len(a)
    while index:
          index-=1
          new_string+=a[index]
    return new_string

print("the reversed string is",reverse(a))

p=int(1000)
print(int(p/10))
#print(p[0])