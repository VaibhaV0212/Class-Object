from abc import ABC, abstractmethod
import math

class Myclass(ABC):
    @abstractmethod
    def calculate(self, x):
        pass

class Sub1(Myclass):
    def calculate(self, x):
        print('Square is ', x*x)

class Sub2(Myclass):
    def calculate(self, x):
        print('Square root is ', math.sqrt(x))

class Sub3(Myclass):
    def calculate(self, x):
        print('Cube is ', x*3)


obj1 = Sub1()
obj1.calculate(45)
print()

obj2 = Sub2()
obj2.calculate(45)
print()

obj3 = Sub3()
obj3.calculate(45)
print()