class FirstClass:
     def init(self,name,salary):
         self.name=name
         self.salary=salary
     def print(self):
         print(self.name)
         print(self.salary)
     def setSalary(self,sal):
         self.salary=sal
     def getSalary(self):
         return self.salary
c=FirstClass()
c.init("joy",10000)
c.print()
c.setSalary(20000)
print(c.getSalary())