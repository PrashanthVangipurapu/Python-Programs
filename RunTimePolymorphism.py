class Vehicle(object):
    wheels=0
    def __init__(self,wheels):
        print("constructor of parent class")
        self.wheels=wheels
    def typeof(self):
          if(self.wheels>2):
              print("heavy")
          else:
              print("light")

class Car (Vehicle):
    def __init__(self,wheels):
        super().__init__(wheels)
        print("constructor of child class")
    def typeof(self):
        super().typeof()
        print("this is child class method")
#print("vehicle has 2 tyres")
'''class Car  (Vehicle):
    def __init__(self,wheels):
        print("child class constructor")
        super().__init__(wheels)
        print("in child class")
    def type(self):
        print("its' a car")'''
class Test:
      c=Car(4)
      c.typeof()
