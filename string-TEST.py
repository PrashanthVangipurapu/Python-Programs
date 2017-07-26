'''my_str=input("enter a string")
print(my_str)
print(type(my_str))
a=int(input("enter a number"))
print(a)
print(type(a))'''

str=input("enter a string")
print(str)
print(str.casefold())
str1=reversed(str)
print(str1)
if(str1==str):
    print("same")

print(str[::-1])
str1=str[::-1]
if(str==str1):
    print("same")

a=int(input())
print(a/2)