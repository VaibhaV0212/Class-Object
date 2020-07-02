'''
A method is called using 2 ways :-
    1. classname.methodname()
    2. instancename.methodname()

__init__ , its a special method used to initialize the variables
that contain data.
'''

class Student:
    def __init__(self):
        self.name = 'VaibhaV'
        self.age = 24
        self.run = 'walk'

    def talk(self):
        print('My name is ', self.name)
        print('My age is ', self.age)

    def walk(self):
        print('I can ', self.run)
s = Student()
s.name
s.age
s.talk()
s.walk()
print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ')

# PROGRAM USING CONSTRUCTOR
class Human:
    def __init__(self, n = '' ,m=0):
        self.name = n
        self.salary = m

    def income(self):
        print('My name is ', self.name)
        print('Salary is ', self.salary)

h = Human()
h.income()
print('-------------')
h = Human('Vaibhav', 22000000)
h.income()
print()