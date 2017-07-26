list1=[10,20,30,40]
print(len(list1))
def sum_fun():
    sum=0;
    for i in list1:
        sum=sum+i
    return sum;

print('sum is',sum_fun())

def mul_fun():
    total=1;
    for i in list1:
        total=total*i;
    return total;
print('multiplication is',mul_fun())


