class Student:
    def __init__(self):
        self.name = 'Obama'
        self.age = 30
        self.marks = 900
    def talk(self):
        print('Hi my name is ', self.name)
        print('Age is', self.age)
        print('Marks are', self.marks)

#create an instance to Student class
s1= Student()
s1.talk()
