class Teacher:
    def setid(self, id):
        self.id = id

    def getid(self):
        return self.id

    def setname(self, name):
        self.name = name

    def getname(self):
        return self.name

t = Teacher()

t.setid(10)
t.setname('Vaib')

print('Your id is ', t.getid())
print('Your name is ', t.getname())
print()

class Student(Teacher):
    def setmarks(self, marks):
        self.marks = marks
    def getmarks(self):
        return self.marks

s = Student()
s.setid(11)
s.setname('Nids')
s.setmarks(900)
print('Id hai ', s.getid())
print('Naam hai ', s.getname())
print('Marks hai ', s.marks)

class Mechnical(Student):
    def setcollege(self, college):
        self.college = college
    def getcollege(self):
        return self.college

m = Mechnical()
m.setcollege('LNCT')
print('My college is ', m.getcollege())