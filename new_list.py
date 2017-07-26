 # This program gives a list of unique values from a list having one or more values of the same number
print("enter the list numbers")
a=input()
a=a.split()
a=[int(i) for i in a]
b=[a[0]]
print("a list is",a)
print("b list is",b)

for x in range(1,len(a)):
    for y in range(0,len(b)):
        if(a[x]==b[y]):
            print("The value of x is",x,"and value of y is",y)
            print("value of a[x] is",a[x],"value of b[y] is",b[y])
            print("b list till now is",b)
            break

    if (y == len(b)-1):   # the inner for loop has iterated the whole b list and didn't found any element that has repeated twice.
        print("entered for checking the last and last but one indexes of b")
        print("b last is",b[y])
        if(a[x]==b[y]):  # checking only for the last element of b list and new element of are equal or not. ex if list is (10 20 30 40 40 50 60 10 20 70 60 80).
            print("you cannot add element")

        else:
            print("You can add a element")
            print("the value of x is",x,"value of a[x] is",a[x])
            b.append(a[x])
            print("b list till now is",b)
    else  :  #loop comes here only when the break occurs. i.e when there is some element coming from a which matched with previous elements of b
        print("you cannot add a element")

        #b.append((a[x]))
        print("b till now is",b)
        print("b's length is",len(b))


print("list a is",a,"and its length is",len(a))
print("list b is",b,"and its length is",len(b))

