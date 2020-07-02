class Sample:

    x = 10    #class variable

    @classmethod     #class method it is called a decorator
    def method(cls):  #cls must be the 1st parameter
        cls.x+=1

s1 = Sample()
s2 = Sample()
print('x in s1', s1.x)
print('x in s2', s2.x)

s1.modify()
print('x in s1', s1.x)
print('x in s2', s2.x)