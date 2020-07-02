class Car:
    wheel = 4   # Class Variable


    def __init__(self):
        self.mil = 10        #Instance variable
        self.com = 'BMW'     #Instance variable


c1 = Car()
c2 = Car()
c1.mil = 8
Car.wheel = 5

print(c1.com, c1.mil, c1.wheel)
print(c2.com, c2.mil)
print('- - - - - - -')

# 2nd Example

class Student:

    section = 12

    def __init__(self):
        self.name = 'VaibhaV'
        self.age = 24

        
s1 = Student()
s2 = Student()
Student.section = 10
print(s1.name, s1.age, Student.section)
print(s2.name, s2.age)
