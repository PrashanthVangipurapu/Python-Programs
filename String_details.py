a=input("enter your string")
u=0
l=0
for x in a:
    if x.isupper():
       u+=1
    if x.islower():
        l+=1
print("The actual string is:",a)
print("number of upper case:",u)
print("number of lower case:",l)