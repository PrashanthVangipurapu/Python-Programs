def fun1(a,b,c=10,d=20):
    res=a+b+c+d;
    return res;
d=fun1(10,20,1000);
print(d)

def fun1(a,b,c,d):
    return a+b+c+d;
print(fun1(20,34,22,22));
#def fun
print(fun1(22,32));

def def_test(a=10,b):
    return a+b;
res=def_test(b=20);
print(res);
