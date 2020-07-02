from abc import *

class Car(ABC):
    def __init__(self, regno):
        self.regno = regno

    def openTank(self):

        print('Fill the fuel for car with regno ', self.regno)

    @abstractmethod
    def steering(self):
        pass

    @abstractmethod
    def braking(self):
        pass
print()

class Maruti(Car):
    def steering(self):
        print('Maruti uses manual steering')
    def braking(self):
        print('Maruti use hydraulic brakes')

m = Maruti('007')
m.openTank()
m.steering()
m.braking()
print('------------')

class Santro(Car):
    def steering(self):
        print('Maruti uses manual steering')
    def braking(self):
        print('Maruti use hydraulic brakes')

s = Santro('1007')
s.openTank()
s.steering()
s.braking()

