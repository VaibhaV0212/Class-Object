class Student:

        #this is a constructor
    def __init__(self, n =' ',m=0):
        self.name = n
        self.age = m

        '''
        this is an instance method
        '''
    def display(self):
        print('Hi', self.name)
        print("Age is", self.age)

#constructor is called without any arguments
s = Student()
s.display()

#constructor is called with 2 arguments
s1 = Student('Pagal', 35)
s1.display()
