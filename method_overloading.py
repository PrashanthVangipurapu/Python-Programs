class Class2:
    def method1(self,name='',salary= 0):
        #print("method overloading-1")
        self.name=name
        self.salary=salary
    def print(self):
        print("name is",self.name)
        print("salary is",self.salary)

c=Class2()
c.method1("joy",10000)
c.print()
print()
c.method1(salary=40000)
c.print()
print()
c.method1(name="roy")
c.print()
