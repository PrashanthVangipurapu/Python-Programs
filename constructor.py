class class3:
    def __init__(self,id):
        self.id=id
        print("constructor called")
    def print(self,name):
        self.name=name
        print("id is",self.id,"name is",self.name)
    '''def __del__(self):
        print("destructor called")'''
c=class3(10)
c.print("roy")
print()
c2=class3(10)
c2.print("roy")

if(c==c2):
    print("both reference same")
else:
    print("diferent referecnes")

